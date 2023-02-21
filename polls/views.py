from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from .models import Poll, Choice, Vote
from .forms import PollAddForm, EditPollForm, ChoiceAddForm
from django.http import HttpResponse


@login_required()
def polls_list(request):
    all_polls = Poll.objects.all()
    all_votes = Vote.objects.all()
    if 'name' in request.GET:
        all_polls = all_polls.order_by('description')

    if 'date' in request.GET:
        all_polls = all_polls.order_by('pub_date')
    
    paginator = Paginator(all_polls, 6)  # Show 6 contacts per page
    paginator2 = Paginator(all_votes, 6)
    page = request.GET.get('page')
    polls = paginator.get_page(page)
    votes = paginator2.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    print(params)
    context = {
        'polls': polls,
        'votes': votes,
        'params': params,
    }
    return render(request, 'polls/polls_list.html', context)


@login_required()
def list_by_user(request):
    all_polls = Poll.objects.filter(owner=request.user)
    all_all_polls = Poll.objects.all()
    all_votes = Vote.objects.filter(user=request.user)
    paginator = Paginator(all_polls, 7)  # Show 7 contacts per page
    paginator2 = Paginator(all_votes, 7)
    paginator3 = Paginator(all_all_polls, 7)

    page = request.GET.get('page')
    polls = paginator.get_page(page)
    votes = paginator2.get_page(page)
    polls_all = paginator3.get_page(page)

    context = {
        'polls': polls,
        'votes': votes,
        'polls_all': polls_all,
    }
    return render(request, 'polls/polls_list.html', context)


@login_required()
def polls_add(request):
    if request.method == 'POST':
        form = PollAddForm(request.POST)
        if form.is_valid:
            poll = form.save(commit=False)
            poll.owner = request.user
            poll.save()
            new_choice1 = Choice(
                poll=poll, choice_description=form.cleaned_data['choice1']).save()
            new_choice2 = Choice(
                poll=poll, choice_description=form.cleaned_data['choice2']).save()

            messages.success(
                request, "Tool added successfully.", extra_tags='alert alert-success alert-dismissible fade show')

            return redirect('polls:list')
    else:
        form = PollAddForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/add_poll.html', context)


@login_required
def polls_edit(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.user != poll.owner:
        return redirect('home')

    if request.method == 'POST':
        form = EditPollForm(request.POST, instance=poll)
        if form.is_valid:
            form.save()
            messages.success(request, "Tool updated successfully.",
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("polls:list")

    else:
        form = EditPollForm(instance=poll)

    return render(request, "polls/poll_edit.html", {'form': form, 'poll': poll})


@login_required
def polls_delete(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.user != poll.owner:
        return redirect('home')
    poll.delete()
    messages.success(request, "Tool deleted successfully.",
                     extra_tags='alert alert-success alert-dismissible fade show')
    return redirect("polls:list")


@login_required
def add_choice(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.user != poll.owner:
        return redirect('home')

    if request.method == 'POST':
        form = ChoiceAddForm(request.POST)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            messages.success(
                request, "Choice added successfully.", extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polls:edit', poll.id)
    else:
        form = ChoiceAddForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/add_choice.html', context)


@login_required
def choice_edit(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    poll = get_object_or_404(Poll, pk=choice.poll.id)
    if request.user != poll.owner:
        return redirect('home')

    if request.method == 'POST':
        form = ChoiceAddForm(request.POST, instance=choice)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            messages.success(
                request, "Choice Updated successfully.", extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polls:edit', poll.id)
    else:
        form = ChoiceAddForm(instance=choice)
    context = {
        'form': form,
        'edit_choice': True,
        'choice': choice,
    }
    return render(request, 'polls/add_choice.html', context)


@login_required
def choice_delete(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    poll = get_object_or_404(Poll, pk=choice.poll.id)
    if request.user != poll.owner:
        return redirect('home')
    choice.delete()
    messages.success(
        request, "Choice Deleted successfully.", extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('polls:edit', poll.id)


def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if not poll.active:
        return render(request, 'polls/poll_result.html', {'poll': poll})
    loop_count = poll.choice_set.count()
    context = {
        'poll': poll,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'polls/poll_detail.html', context)


@login_required
def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    choice_id = request.POST.get('choice')
    if not poll.user_can_vote(request.user): # restore case
        # delete vote
        vote = Vote.objects.get(user=request.user, poll=poll)
        vote.delete()
        
        poll.active = True
        poll.save()
        return render(request, 'polls/poll_result.html', {'poll': poll})

    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        vote = Vote(user=request.user, poll=poll, choice=choice)
        vote.save()
        if poll.active is True:
            poll.active = False
            poll.save()
        print(vote)
        return render(request, 'polls/poll_result.html', {'poll': poll})
    else:
        return redirect("polls:detail", poll_id)
    return render(request, 'polls/poll_result.html', {'poll': poll})


@login_required
def endpoll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.user != poll.owner:
        return redirect('home')

    if poll.active is True:
        poll.active = False
        poll.save()
        return render(request, 'polls/poll_result.html', {'poll': poll})
    else:
        return render(request, 'polls/poll_result.html', {'poll': poll})

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Poll, Choice, Vote


class PollTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.poll = Poll.objects.create(
            owner=self.user,
            description='Test poll',
            pub_date=timezone.now()
        )
        self.choice1 = Choice.objects.create(
            poll=self.poll,
            choice_description='Choice 1'
        )
        self.choice2 = Choice.objects.create(
            poll=self.poll,
            choice_description='Choice 2'
        )

    def test_user_can_vote(self):
        """Test that user_can_vote() returns False when user already voted"""
        vote = Vote.objects.create(
            user=self.user,
            poll=self.poll,
            choice=self.choice1
        )
        self.assertFalse(self.poll.user_can_vote(self.user))

    def test_get_vote_count(self):
        """Test that get_vote_count returns correct number of votes"""
        vote1 = Vote.objects.create(
            user=self.user,
            poll=self.poll,
            choice=self.choice1
        )
        vote2 = Vote.objects.create(
            user=self.user,
            poll=self.poll,
            choice=self.choice2
        )
        self.assertEqual(self.poll.get_vote_count, 2)

    def test_get_result_dict(self):
        """Test that get_result_dict() returns the expected result"""
        Vote.objects.create(
            user=self.user,
            poll=self.poll,
            choice=self.choice1
        )
        Vote.objects.create(
            user=self.user,
            poll=self.poll,
            choice=self.choice2
        )
        result_dict = self.poll.get_result_dict()
        self.assertEqual(len(result_dict), 2)
        self.assertEqual(result_dict[0]['num_votes'], 1)
        self.assertEqual(result_dict[1]['num_votes'], 1)

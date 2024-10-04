from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Follow

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='Test Bio')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'Test Bio')

class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.follow = Follow.objects.create(follower=self.user1, following=self.user2)

    def test_follow_creation(self):
        self.assertEqual(self.follow.follower.username, 'testuser1')
        self.assertEqual(self.follow.following.username, 'testuser2')
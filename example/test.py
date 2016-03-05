from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from actstream import action
from .models import Notification


class NotificationModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='test@example.com.com', password='password')

    def test_signup_form_fields(self):
        notification = Notification.objects.create(text='Hello world!')
        action.send(self.user, verb='was notified', action_object=notification)

        self.client.force_login(self.user)
        feed_url = reverse('notification_feed_json')

        response = self.client.get(feed_url)
        print(response.content)

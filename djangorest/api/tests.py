# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Message
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.message_data = {'message_text': 'hola hallo hola'}
        self.response = self.client.post(
            reverse('create'),
            self.message_data,
            format="json",
        )

    def test_create_message(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_message(self):
        message = Message.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': message.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, message)

    def test_update_message(self):
        message = Message.objects.get()
        change_message = {'message_text': 'welcome welcome welcome'}
        response = self.client.put(
            reverse('details', kwargs={'pk': message.id}),
            change_message,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_message(self):
        message = Message.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': message.id}),
            format="json",
            follow=True,
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class ModelTestCase(TestCase):
    def setUp(self):
        self.message_text = "hello hello hello"
        self.message = Message(message_text = self.message_text)

    def test_model_create_message(self):
        count_pre = Message.objects.count()
        self.message.save()
        count_post = Message.objects.count()
        self.assertNotEqual(count_pre, count_post)

from django.test import TestCase
from rest_framework.test import APIRequestFactory
import random
from django.urls import reverse
from rest_framework import status
from core.models import Test

class FirstTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        # return super().setUp()

    def test_post(self):
        """
            Ensure we can create a new account object.
        """
        url = reverse('test')
        data = {'snake_value': 1}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Test.objects.count(), 1)
        self.assertEqual(Test.objects.get().snake_value, 1)

if __name__=='__main__':
    t = FirstTestCase()
    t.test_post()

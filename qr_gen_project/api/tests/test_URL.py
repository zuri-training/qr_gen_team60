from django.test import TestCase, Client
from django.urls import reverse

# import requests


#TODO: Fix this tests later
class QRGeneratorURLTest(TestCase):
        def test_home_url(self):
            response = self.client.get("/qr-gen/api")
            self.assertEqual(response.status_code, 200)

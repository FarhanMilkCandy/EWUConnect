from logging import setLogRecordFactory
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserModel
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'email' : 'test@testmail.com',
            'name' : 'Test User',
            'password1' : 'testpass',
            'password2' : 'testpass'
        }
        self.invalid_user = {
            'email' : 'test@test.com',
            'name' : 'Test User',
            'password1' : 'testpass23',
            'password2' : 'testpass'
        }
        return super().setUp()

    def test_registration_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/Registration.html')
    
    def test_registers_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/Registration.html')
    
    def test_invalid_registers_user(self):
        response = self.client.post(self.register_url, self.invalid_user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/Registration.html')
    
    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
    
    # def test_can_login(self):
    #     response = self.client.post(self.register_url, self.user, format='text/html')
    #     user = UserModel.objects.filter(email = self.user['email']).first()
    #     user.is_active = True
    #     user.save()
    #     response = self.client.post(self.login_url, self.user, format='text/html')
    #     self.assertEqual(response.status_code, 200) 

    


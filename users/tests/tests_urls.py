from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views


class Test_urls(SimpleTestCase):
    def test_register_url_resolve(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, views.signup_view)

    def test_login_url_resolve(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, views.login_view)

    def test_logout_url_resolve(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, views.logout_view)
    
    def test_profile_url_resolve(self):
        url = reverse("profile", args=['1'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, views.profile_view)

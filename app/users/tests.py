import os
import django

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse

from .models import Profile, ProfileAdmin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'journal_dobrynya.settings')
django.setup()

class UserViewsTest(TestCase):
    def setUp(self) -> None:
        self.client: Client = Client()

        self.user: User = User.objects.create_user(username="testuser", password="12345")
        self.superuser: User = User.objects.create_superuser(username="admin", password="12345")
        self.profile: Profile = Profile.objects.create(user=self.user)
        self.profile_admin: ProfileAdmin = ProfileAdmin.objects.create(user=self.superuser)

    def test_user_login_view(self) -> None:
        response: HttpResponse = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users.login_register.html")

    def test_user_login_authentication(self) -> None:
        response: HttpResponse = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "12345"
            }
        )
        self.assertRedirects(response, reverse("home"))

    def test_user_logout_view(self) -> None:
        self.client.login(username='testuser', password='12345')
        response: HttpResponse = self.client.get(reverse("user_logout"))
        self.assertRedirects(response, reverse("login"))

    def test_user_register_view_get(self) -> None:
        response: HttpResponse = self.client.get(reverse("user_register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login_register.html")

    def test_user_register_view_post(self) -> None:
        response: HttpResponse = self.client.post(reverse("user_register"), {
            "username": "newuser",
            "password1": "password12345",
            "password2": "password12345",
            "email": "newuser@example.com"
        })
        self.assertRedirects(response, reverse("login"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_all_users_view(self) -> None:
        self.client.login(username='testuser', password='12345')
        response: HttpResponse = self.client.get(reverse("all_users"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/users.html")
        self.assertContains(response, self.user.username)

    def test_all_coach_view(self) -> None:
        self.client.login(username='admin', password='12345')
        response: HttpResponse = self.client.get(reverse("all_coach"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/all_coach.html")
        self.assertContains(response, self.superuser.username)

    def test_profile_view(self) -> None:
        self.client.login(username='testuser', password='12345')
        response: HttpResponse = self.client.get(reverse("profile", kwargs={"pk": self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")
        self.assertContains(response, self.user.username)

    def test_user_questionnaire_view(self) -> None:
        self.client.login(username='testuser', password='12345')
        response: HttpResponse = self.client.get(reverse("user_questionnaire"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/questionnaire.html")

    def test_edit_admin_profile_view_superuser(self) -> None:
        self.client.login(username='admin', password='12345')
        response: HttpResponse = self.client.get(reverse("edit_admin_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/questionnaire.html")

    def test_edit_admin_profile_view_not_superuser(self) -> None:
        self.client.login(username='testuser', password='12345')
        response: HttpResponse = self.client.get(reverse("edit_admin_profile"))
        self.assertRedirects(response, reverse("home"))

    def test_personal_data_view(self) -> None:
        response: HttpResponse = self.client.get(reverse("personal_data"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/personal_data.html")

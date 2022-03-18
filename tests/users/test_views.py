from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from diary.models import Post
from users.models import Resident


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="Django321",
        )
        self.resident = Resident.objects.create(
            last_name="last",
            first_name="first",
            birth_date="2000-02-02",
            place_of_birth="Birth",
            secret_information="secret",
            surgeries="surgeries",
            treating_doctor="treating",
            medical_treatment="medical",
            entry_date="2000-02-02",
        )
        self.post = Post.objects.create(
            title="title_of_the_post",
            author=self.user,
            content="content",
            resident=self.resident,
        )
        # self.register_page_url = reverse("register")
        self.profile_page_url = reverse("profile")
        self.login_page_url = reverse("login")
        self.logout_page_url = reverse("logout")
        self.password_reset_page_url = reverse("password_reset")
        self.password_reset_done_page_url = reverse("password_reset_done")
        self.password_reset_complete_page_url = reverse("password_reset_complete")
        self.user_residents_page_url = reverse("user-residents")
        self.substitute_resident_detail_url = \
            reverse("resident-detail", args=[1])
        self.users_list_page_url = reverse("users")
        self.relatives_list_page_url = reverse("relatives")
        self.relative_profiles_page_url = \
            reverse("relative-profiles", args=[self.user.id])

    # def test_register_page(self):
    #     response = self.client.get(self.register_page_url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "users/register.html")

    def test_profile_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.profile_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")

    def test_login_page(self):
        response = self.client.get(self.login_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_logout_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.logout_page_url)

        self.assertEqual(response.status_code, 200)

    def test_password_reset_page(self):
        response = self.client.get(self.password_reset_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset.html")

    def test_password_reset_done_page(self):
        response = self.client.get(self.password_reset_done_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset_done.html")

    def test_password_reset_complete_page(self):
        response = self.client.get(self.password_reset_complete_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/password_reset_complete.html")

    def test_resident_detail_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_resident_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/resident_detail.html")

    def test_users_list_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.users_list_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/users.html")

    def test_relatives_list_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.relatives_list_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/relatives.html")

    def test_relative_profiles_list_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.relative_profiles_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/relative_profiles.html")

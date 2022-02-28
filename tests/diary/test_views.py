from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from diary.models import Post
from users.models import Resident


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user",
            email="user@gmail.com",
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
        self.home_page_url = reverse("diary-home")
        self.posts_list_page_url = reverse("diary-post")
        self.posts_list_page_url = reverse("diary-post")
        self.substitute_post_url = \
            reverse("post-detail", args=[1])
        self.substitute_user_posts_list_url = \
            reverse("user-posts", args=[self.user.username])
        self.substitute_post_create_url = \
            reverse("post-create", args=[1])
        self.substitute_post_update_url = \
            reverse("post-update", args=[1])
        self.substitute_post_delete_url = \
            reverse("post-delete", args=[1])
        self.substitute_resident_posts_list_url = \
            reverse("resident-posts", args=[1])


    def test_home_page(self):
        response = self.client.get(self.home_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/home.html")

    def test_posts_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.posts_list_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/posts.html")

    def test_user_posts_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_user_posts_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/user_posts.html")

    def test_post_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_post_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/post_detail.html")

    def test_post_create_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_post_create_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/post_form.html")

    def test_post_update_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_post_update_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/post_form.html")

    def test_post_delete_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_post_delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/post_confirm_delete.html")

    def test_resident_posts_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.substitute_resident_posts_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/resident_posts.html")

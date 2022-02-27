from django.test import TestCase
from django.contrib.auth.models import User
from diary.models import Post
from users.models import Resident


class ModelsTestsCase(TestCase):

    def test_post_table(self):
        user = User.objects.create(
            username="user",
            email="user@gmail.com",
            password="Django321",
        )
        resident = Resident.objects.create(
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
        post = Post.objects.create(
            title="title_of_the_post",
            author=user,
            content="content",
            resident=resident,
        )
        self.assertEqual(post.title, "title_of_the_post")

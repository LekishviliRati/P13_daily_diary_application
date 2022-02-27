from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Resident, Profile


class ModelsTestsCase(TestCase):

    def test_user_email(self):
        user = User.objects.create(
            username="user",
            email="user@gmail.com",
            password="Django321",
        )
        self.assertEqual(user.email, "user@gmail.com")

    def test_superuser_is_superuser(self):
        superuser = User.objects.create_superuser(
            username="superuser",
            email="superuser@gmail.com",
            password="Django321",
        )
        self.assertIs(superuser.is_superuser, True)

    def test_user_not_superuser(self):
        user = User.objects.create_user(
            username="superuser",
            email="user@gmail.com",
            password="Django321",
        )
        self.assertIs(user.is_superuser, False)

    def test_resident_table(self):
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
        self.assertEqual(resident.last_name, "last")

    def test_profile_table(self):
        user = User.objects.create(
            username="user1",
            email="user1@gmail.com",
            password="Django321",
        )
        # "Pas renseigné" is de default value of user.profile.address
        self.assertEqual(user.profile.address, "Pas renseigné")



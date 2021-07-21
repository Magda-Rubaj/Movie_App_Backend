from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import UserView
from .models import User

class ListUserTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserView.as_view(actions={'post': 'create', 'get': 'list'})

        self.valid_user = {
            'email' : 'testuser@email.com',
            'password' : 'password'
        }

        self.invalid_user_email = {
            'email' : 'testuser@email',
            'password' : 'password'
        }

        self.invalid_user_field = {
            'email' : 'testuser@email',
            'password' : 'password'
        }

        self.regular_user = User.objects.create_user(
            email='example@example.com', 
            password='pass'
        )

        self.admin_user = User.objects.create_user(
            email='admin@example.com', 
            password='pass', 
            is_admin=True
        )

    def test_post_valid_user(self):
        request = self.factory.post('/users/', self.valid_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
    
    def test_post_invalid_user_email(self):
        request = self.factory.post('/users/', self.invalid_user_email)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_user_field(self):
        request = self.factory.post('/users/', self.invalid_user_field)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
    
    def test_get_as_regular_list(self):
        request = self.factory.get('/users/')
        force_authenticate(request, user=self.regular_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 403)
    
    def test_get_as_admin_list(self):
        request = self.factory.get('/users/')
        force_authenticate(request, user=self.admin_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
    

class DetailUserTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        self.regular_user = User.objects.create_user(
            email='example@example.com', 
            password='pass'
        )

        self.admin_user = User.objects.create_user(
            email='admin@example.com', 
            password='pass', 
            is_admin=True
        )

        self.view = UserView.as_view(actions={'get': 'retrieve'})

    def test_unauth_self(self):
        request = self.factory.get('/users/{0}/'.format(self.regular_user.id))
        response = self.view(request)
        self.assertEqual(response.status_code, 401)

    def test_auth_self(self):
        request = self.factory.get('/users/{0}/'.format(self.regular_user.id))
        force_authenticate(request, user=self.regular_user)
        response = self.view(request, pk=self.regular_user.pk)
        self.assertEqual(response.status_code, 200)

    def test_as_regular_another_user(self):
        request = self.factory.get('/users/{0}/'.format(self.admin_user.id))
        force_authenticate(request, user=self.regular_user)
        response = self.view(request, pk=self.admin_user.pk)
        self.assertEqual(response.status_code, 403)
    
    def test_as_admin_another_user(self):
        request = self.factory.get('/users/{0}/'.format(self.regular_user.id))
        force_authenticate(request, user=self.admin_user)
        response = self.view(request, pk=self.regular_user.pk)
        self.assertEqual(response.status_code, 200)


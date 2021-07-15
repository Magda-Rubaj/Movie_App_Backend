from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import UserView
from .models import User

class PostUserTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserView.as_view(actions={'post': 'create'})

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

    def test_valid_user(self):
        request = self.factory.post('/users/', self.valid_user)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
    
    def test_invalid_user_email(self):
        request = self.factory.post('/users/', self.invalid_user_email)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_user_field(self):
        request = self.factory.post('/users/', self.invalid_user_field)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
    
class GetUserTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(email='example@example.com', password='pass')
        self.view = UserView.as_view(actions={'get': 'retrieve'})

    def test_unauthorized_self(self):
        request = self.factory.get('/users/{0}/'.format(self.user.id))
        response = self.view(request)
        self.assertEqual(response.status_code, 401)

    def test_authorized_self(self):
        request = self.factory.get('/users/{0}/'.format(self.user.id))
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, 200)


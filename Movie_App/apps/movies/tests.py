from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import MovieView
from .models import Movie
from apps.accounts.models import User


class ListMovieTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = MovieView.as_view(actions={'post': 'create', 'get': 'list'})

        self.user = User.objects.create_user(
            email='example@example.com', 
            password='pass'
        )

        self.movie =  {
            'title' : 'TestTitle',
            'production_year' : 2020,
            'description' : 'Some test movie',
            'added_by' : self.user.id
        }

    def test_unauth_post(self):
        request = self.factory.post('/movies/', self.movie)
        response = self.view(request)
        self.assertEqual(response.status_code, 401)
    
    def test_auth_post(self):
        request = self.factory.post('/movies/', self.movie)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
    
    def test_get_all(self):
        request = self.factory.get('/movies/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)


class DetailMovieTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = MovieView.as_view(actions={'get': 'retrieve'})

        self.regular_user = User.objects.create_user(
            email='example@example.com', 
            password='pass'
        )

        self.admin_user = User.objects.create_user(
            email='admin@example.com', 
            password='pass', 
            is_admin=True
        )

        self.movie_owned_regular = Movie.objects.create(
            title='TestTitle',
            production_year=2020,
            description='Some test movie',
            added_by=self.regular_user
        )

        self.movie_owned_admin = Movie.objects.create(
            title='TestTitle',
            production_year=2020,
            description='Some test movie',
            added_by=self.admin_user
        )
    
    def test_regular_owner(self):
        request = self.factory.get('/movies/{0}/'.format(self.movie_owned_regular.id))
        force_authenticate(request, user=self.regular_user)
        response = self.view(request, pk=self.movie_owned_regular.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_regular_not_owner(self):
        request = self.factory.get('/movies/{0}/'.format(self.movie_owned_admin.id))
        force_authenticate(request, user=self.regular_user)
        response = self.view(request, pk=self.movie_owned_admin.pk)
        self.assertEqual(response.status_code, 403)
    
    def test_admin(self):
        request = self.factory.get('/movies/{0}/'.format(self.movie_owned_regular.id))
        force_authenticate(request, user=self.admin_user)
        response = self.view(request, pk=self.movie_owned_regular.pk)
        self.assertEqual(response.status_code, 200)

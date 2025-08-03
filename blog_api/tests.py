from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User

class PostAPITests(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user( 
            username='test_user1',
            password='123456789'
        )
        data = {
            'title': 'new title',
            'excerpt': 'new Post Excerpt',
            'slug': 'new post-title',
            'content': 'new Post Content',
            'category': self.test_category.id,
            'author': 1,
            'status': 'published'
        }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from posts.models import Post, Comment

User = get_user_model()

class PostCommentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_post_and_comment(self):
        # Create post
        res = self.client.post('/api/posts/', {'title': 'T1', 'content': 'C1'}, format='json')
        self.assertEqual(res.status_code, 201)
        post_id = res.data['id']

        # Create comment
        res2 = self.client.post('/api/comments/', {'post': post_id, 'content': 'Nice!'}, format='json')
        self.assertEqual(res2.status_code, 201)

        # List post comments
        res3 = self.client.get(f'/api/posts/{post_id}/comments/')
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(len(res3.data['results']), 1)

    def test_only_owner_can_edit_post(self):
        post = Post.objects.create(author=self.user, title='Mine', content='x')
        other = User.objects.create_user(username='bob', password='pass123')
        c2 = APIClient()
        c2.force_authenticate(other)
        res = c2.patch(f'/api/posts/{post.id}/', {'title': 'Hacked'}, format='json')
        self.assertEqual(res.status_code, 403)

def test_like_and_unlike(self):
    res = self.client.post(f'/api/posts/{self.post.id}/like/')
    self.assertEqual(res.status_code, 201)
    res2 = self.client.post(f'/api/posts/{self.post.id}/like/')
    self.assertEqual(res2.status_code, 400)  # cannot like twice
    res3 = self.client.post(f'/api/posts/{self.post.id}/unlike/')
    self.assertEqual(res3.status_code, 200)

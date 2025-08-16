from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostCrudTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="StrongPass123!")
        self.bob = User.objects.create_user(username="bob", password="AnotherPass123!")
        self.post = Post.objects.create(title="Hello", content="World", author=self.alice)

    def test_list_and_detail_public(self):
        list_resp = self.client.get(reverse('post-list'))
        self.assertEqual(list_resp.status_code, 200)
        detail_resp = self.client.get(reverse('post-detail', args=[self.post.pk]))
        self.assertEqual(detail_resp.status_code, 200)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertEqual(resp.status_code, 302)  # redirect to login

        self.client.login(username="alice", password="StrongPass123!")
        resp = self.client.post(reverse('post-create'), {"title": "New", "content": "Post"})
        self.assertEqual(Post.objects.count(), 2)

    def test_only_author_can_edit_delete(self):
        # Bob cannot edit Alice's post
        self.client.login(username="bob", password="AnotherPass123!")
        resp = self.client.get(reverse('post-edit', args=[self.post.pk]))
        self.assertEqual(resp.status_code, 403)  # UserPassesTestMixin returns 403 by default

        # Author can edit
        self.client.login(username="alice", password="StrongPass123!")
        resp = self.client.post(reverse('post-edit', args=[self.post.pk]), {"title": "Edited", "content": "Changed"})
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Edited")

        # Author can delete
        resp = self.client.post(reverse('post-delete', args=[self.post.pk]))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

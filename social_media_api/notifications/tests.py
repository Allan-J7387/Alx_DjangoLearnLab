def test_notifications_list(self):
    Notification.objects.create(recipient=self.user, actor=self.user, verb="test")
    res = self.client.get('/api/notifications/')
    self.assertEqual(res.status_code, 200)
    self.assertGreaterEqual(len(res.data), 1)

import unittest

class BlogTest(unittest.TestCase):
    def test_user_login(self):
        self.assertEqual(userLogin(), 'login successful!')

    def test_user_logout(self):
        self.assertEqual(userLogout(), 'Thank you!')

    def test_user_edit(self):
        self.assertEqual(Edit(), 'Edited!')

    def test_user_create(self):
        self.assertEqual(Create(), 'Created!')

    def test_moderator_edit(self):
        self.assertEqual(Edit(), 'Edited!')

    def test_moderator_delete(self):
        self.assertEqual(Delete(), 'Deleted!')

    def test_admin_delete(self):
        self.assertEqual(Delete(), 'Deleted!')

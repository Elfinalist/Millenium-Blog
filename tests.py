import unittest
from models.user import User
class BlogTest(unittest.TestCase):
    def test_user_login(self):
        self.assertEqual(User().login(), 'login successful!')

    def test_user_logout(self):
        self.assertEqual(User().logout(), 'Thank you!')

    def test_user_edit(self):
        self.assertEqual(User().edit_comment(), 'Edited!')


    # def test_user_create(self):
    #     self.assertEqual(User().create_comment(), 'Created!')

    # def test_moderator_edit(self):
    #     self.assertEqual(User().edit_comment(), 'Edited!')

    # def test_moderator_delete(self):
    #     self.assertEqual(Delete(), 'Deleted!')

    # def test_admin_delete(self):
    #     self.assertEqual(Delete(), 'Deleted!')


if __name__ == "__main__":
    unittest.run()

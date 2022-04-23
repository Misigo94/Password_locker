import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Alex","Kamau","0712345678","alex@gmail.com")

    def test__init(self):
        self.assertEqual(self.new_user.first_name,"Alex")
        self.assertEqual(self.new_user.last_name,"Kamau")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"alex@gmail.com")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        self.new_user.save_user()
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
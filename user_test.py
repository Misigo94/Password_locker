import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        method that allows us to define instructions which will be executed before each test
        '''
        self.new_user = User("Alex","Kamau","0712345678","alex@gmail.com")

    def test__init(self):
        '''
        test case that tests if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Alex")
        self.assertEqual(self.new_user.last_name,"Kamau")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"alex@gmail.com")

    # def test_save_user(self):
    #     self.new_user.save_user()
    #     self.assertEqual(len(User.user_list),1)

    # def test_delete_user(self):
    #     self.new_user.save_user()
    #     self.assertEqual()

if __name__ == '__main__':
    unittest.main()
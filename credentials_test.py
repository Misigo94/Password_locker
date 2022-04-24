import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials("Alex94","Alex94")

    def test__init(self):
        self.assertEqual(self.new_credentials.user_name,"Alex94")
        self.assertEqual(self.new_credentials.password,"Alex94")

    def test_save_credentials(self):
        self.new_credentials.save_credentials
        self.assertEqual(len(Credentials.credentials_list),0)


if __name__ =='__main__':
    unittest.main()

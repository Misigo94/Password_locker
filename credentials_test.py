
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    test clas that defines test for credentials class
    '''
    
    def setUp(self):
        '''
        method that allows us to define a set of instructions to be executed before each test
        '''
        self.new_credentials = Credentials("Alex94","Alex94")

    def test__init(self):
        '''
        test method that allows us to maek sure that objects have been initalized properly
        '''
        self.assertEqual(self.new_credentials.user_name,"Alex94")
        self.assertEqual(self.new_credentials.password,"Alex94")

    def test_save_credentials(self):
        '''
        test to test if the the credentials objects is saved into the credentials_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_several_credentials(self):
        '''
        method that adds multiple credentials to credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Martin","1234")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        method to test if we can remove a credentail from the credential_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Martin","1234")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_name(self):
        '''
        method test to check if we can find the credentials of the user
        '''
        self.new_credentials.save_credentials()
        test_credentials= Credentials("Martin","1234")
        test_credentials.save_credentials()
        # found.credentials = Credentials.find_by_name("Martin")
        # self.assertEqual(found_credentials.user_name,
        # test_credentials.user_name)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ =='__main__':
    unittest.main()

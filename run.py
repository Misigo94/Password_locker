import random
from credentials import Credentials
from user import User

def create_credential(user_name,password):
    '''
    function to create a new credential
    '''
    new_credential = Credentials(user_name,password)

def save_credential(credential):
    '''
    function to save contact
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    function to delete a credential
    '''
    credential.delete_credential()

def find_credential(credential):
    return Credentials.find_by_name(user_name)
    
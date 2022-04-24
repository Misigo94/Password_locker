
class Credentials:
    '''
    class that generates new instaces of user credentials of their accounts
    '''

    credentials_list=[]

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        '''
        method that stores new credentials into credentials_list
        '''
        Credentials.credentials_list.append(self)

    # def save__several_credentials(self):
    #     Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        method that removes credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self) 

    @classmethod
    def find_by_name(cls,user_name):
        '''
        method that takes in a name and returns credential that has that number
        Args:
         name:user_name to search for
         Return:
         The user_name and its password
        '''
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                return credential

    @classmethod
    def credential_exist(cls,name):
        '''
        method tha checks if credential exists
        Args:
            name: acc_name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credential in cls.credential_exist:
            if credential.user_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        methos that returns the credentials list
        '''
        return cls.credentials_list



        

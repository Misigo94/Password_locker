
class Credentials:

    credentials_list=[]

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

        

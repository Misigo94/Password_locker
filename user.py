
class User:
    '''
    class that creates new instances of users
    '''
    user_list=[]

    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email

    def save_user(self):
        '''
        functions that saves user objects to the user_list
        '''
        User.user_list.append(self)

    # def delete__user(self):
    #     User.user_list.remove(self)
        
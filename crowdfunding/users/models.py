from django.contrib.auth.models import AbstractUser # abstract user model allows us to customize the user model
''' Setting up a CustomUser model provide a flexible and extensible way to manage

user authentication and data within a Django project. It allows for customistion, 

future proofing, authentication flexibility and data organization. It is also best practice

'''

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

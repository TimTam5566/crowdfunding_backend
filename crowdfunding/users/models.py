from django.contrib.auth.models import AbstractUser # abstract user model allows us to customize the user model

class CustomUser (AbstractUser):

    def __str__(self):
        return self.username

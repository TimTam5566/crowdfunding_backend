from django.db import models
from django.contrib.auth import get_user_model # Import the custom user model doing this wires up some django magic

''' Imports let us define our own models and safely reference the user model for relationships'''

class Fundraiser(models.Model): #starts the definition of the fundraiser model which will be used by django to create a database table
   
   ''' Stores information about each fundraiser campaign '''
   
   description = models.TextField()
   goal = models.IntegerField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True)
   owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE, # if user gets deleted, fundraisers get deleted
      related_name='owned_fundraisers'   
   )
   
class Pledge(models.Model):

   ''' Stores information about each pledge towards a campaign'''

   amount = models.IntegerField()
   comment = models.CharField(max_length=200)
   anonymous = models.BooleanField()
   fundraiser = models.ForeignKey(
      'Fundraiser',
      on_delete=models.CASCADE,
      related_name='pledges'   
   )
   supporter = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE, # if user gets deleted pledges get deleted
      related_name='pledges'  
   )

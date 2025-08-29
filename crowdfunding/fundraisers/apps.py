from django.apps import AppConfig

'''Configures the fundraisers app and tells Django how to handle it internally '''

class FundraisersConfig(AppConfig): # defines configuration class for Fundraisers app, used to set up and identify app
    default_auto_field = 'django.db.models.BigAutoField' # sets the default type for auto-incrementing primary keys on models to BigAutoField (a 64-bit integer)
    name = 'fundraisers'

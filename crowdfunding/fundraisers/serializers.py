from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta: #  job is to serialize our Fundraiser model into JSON, and that it should include __all__ of the fields when it does so!
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta: #  job is to serialize our Fundraiser model into JSON, and that it should include __all__ of the fields when it does so!
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'
        # This serializer will convert Pledge model instances into JSON format, and vice versa.
        # It will include all fields defined in the Pledge model.

class FundraiserDetailSerializer(FundraiserSerializer): # adding unctionality to the FundraiserDetail view
    pledges = PledgeSerializer(many=True, read_only=True)  # This will include the related pledges in the serialized data

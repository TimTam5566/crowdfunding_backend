from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta: #  job is to serialize our Fundraiser model into JSON, and that it should include __all__ of the fields when it does so!
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'
        # This serializer will convert Pledge model instances into JSON format, and vice versa.
        # It will include all fields defined in the Pledge model.

class FundraiserDetailSerializer(FundraiserSerializer): # adding unctionality to the FundraiserDetail view
    pledges = PledgeSerializer(many=True, read_only=True)  # This will include the related pledges in the serialized data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = instance.date_created('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
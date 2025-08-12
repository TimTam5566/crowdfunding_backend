from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Fundraiser # Import our Fundraiser model
from .serializers import FundraiserSerializer # Import our FundraiserSerializer

# Create your views here.

class FundraiserList(APIView): # inheriting from APIView to create a view for listing fundraisers

    def get(self, request):
        fundraisers = Fundraiser.objects.all() # Fetch all Fundraiser objects from the database
    
        serializer = FundraiserSerializer(fundraisers, many=True) # converts database list to JSON format
        
        return Response(serializer.data) # Return the serialized data as a response

    def post(self, request): # Method to handle POST requests for creating new fundraisers
        serializer = FundraiserSerializer(data=request.data) # we use the serializer to convert it to a Fundraiser model instance.
        if serializer.is_valid(): # If the data was valid, 
            serializer.save() # the serializer then saves the model instance to the database.
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
                ) # 201 CREATED if the request was successful
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
             ) # If the data was invalid, we return a 400 BAD REQUEST with the errors.
    
class FundraiserDetail(APIView):
   
    def get_object(self, pk): # pk (Primary Key). This variable will hold the primary key of the record being retrieved. # This defines how to retrieve the correct object from the database, based on a primary key (pk)
            
        try:
            fundraiser = Fundraiser.objects.get(pk=pk) # get: This defines the behaviour that should result from a GET request. 
            
            return fundraiser
        
        except Fundraiser.DoesNotExist: # try/except block. This allows us to define an "expected" behaviour, and a "backup" behaviour if we encounter errors. 
            
            raise Http404 #  if no fundraiser exists in the database that has the supplied primary key value, we raise an "exception" that results in a 404 NOT FOUND result being returned to the user.

    def get(self, request, pk):
      
       fundraiser = self.get_object(pk)
       
       serializer = FundraiserSerializer(fundraiser)
       
       return Response(serializer.data)
    

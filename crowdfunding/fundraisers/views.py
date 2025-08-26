from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Fundraiser, Pledge # Import our Fundraiser model
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer # Import our FundraiserSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class FundraiserList(APIView): # inheriting from APIView to create a view for listing fundraisers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        fundraisers = Fundraiser.objects.all() # Fetch all Fundraiser objects from the database
        serializer = FundraiserSerializer(fundraisers, many=True) # converts database list to JSON format
        return Response(serializer.data) # Return the serialized data as a response

    def post(self, request): # Method to handle POST requests for creating new fundraisers
        serializer = FundraiserSerializer(data=request.data) # we use the serializer to convert it to a Fundraiser model instance.
        if serializer.is_valid(): # If the data was valid, 
            serializer.save(owner=request.user) # the serializer then saves the model instance to the database.
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
                ) # 201 CREATED if the request was successful
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
                ) # If the data was invalid, we return a 400 BAD REQUEST with the errors.
    
class FundraiserDetail(APIView):
    permission_classs = [
        permissions.IsAuthenticatedOrReadOnly, # Allow read-only access for unauthenticated users, but restrict write access to authenticated users.
        IsOwnerOrReadOnly # Custom permission to allow only owners of an object to edit it.
    ]

    def get_object(self, pk): # pk (Primary Key). This variable will hold the primary key of the record being retrieved. # This defines how to retrieve the correct object from the database, based on a primary key (pk)    
        try:
            fundraiser = Fundraiser.objects.get(pk=pk) # get: This defines the behaviour that should result from a GET request. 
            self.check_object_permissions(self.request, fundraiser) # This line checks if the user has the necessary permissions to access or modify the fundraiser object.
            return fundraiser
        
        except Fundraiser.DoesNotExist: # try/except block. This allows us to define an "expected" behaviour, and a "backup" behaviour if we encounter errors. 
            raise Http404 #  if no fundraiser exists in the database that has the supplied primary key value, we raise an "exception" that results in a 404 NOT FOUND result being returned to the user.

    def get(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)
    
    def put(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()  # Fetch all Pledge objects from the database
        serializer = PledgeSerializer(pledges, many=True)  # Convert database list to JSON format
        return Response(serializer.data)  # Return the serialized data as a response

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)  # Convert request data to a Pledge model instance
        if serializer.is_valid():  # If the data is valid
            serializer.save(supporter=request.user)  # Save the model instance to the database
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
                )  # Return 201 CREATED if successful
        else:
            return Response(
                serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                )  # Return 400 BAD REQUEST if invalid data

    


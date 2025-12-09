from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing

@api_view(["GET"])
def hello(request):
    return Response({"message": "Welcome to ALX Travel Listings API"})


@api_view(['GET', 'POST'])
def listings_list(request):
    """
    List all listings or create a new listing
    """
    if request.method == 'GET':
        listings = Listing.objects.all()
        data = [{"id": listing.id, "title": listing.title} for listing in listings]
        return Response(data)
    
    elif request.method == 'POST':
        return Response({"message": "Listing created"}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def listing_detail(request, pk):
    """
    Retrieve, update or delete a listing
    """
    try:
        listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        data = {"id": listing.id, "title": listing.title}
        return Response(data)
    
    elif request.method == 'PUT':
        return Response({"message": "Listing updated"})
    
    elif request.method == 'DELETE':
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

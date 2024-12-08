from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from django.views.decorators.csrf import csrf_exempt
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from alx_travel_app.listings.models import Listing
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


from alx_travel_app.listings.serializers import ListingSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    """
    queryset = Listing.objects.all().order_by('name')
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]

# @csrf_exempt
# def listing_detail(request, pk):
#     """
#     Retrieve, update or delete a code listing.
#     """
#     try:
#         listing = Listing.objects.get(pk=pk)
#     except Listing.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ListingSerializer(listing)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ListingSerializer(listing, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         listing.delete()
#         return HttpResponse(status=204)

# @csrf_exempt
# def listings_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         listings = Listing.objects.all()
#         serializer = ListingSerializer(listings, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ListingSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

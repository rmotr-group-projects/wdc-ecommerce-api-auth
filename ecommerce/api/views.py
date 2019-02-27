from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.models import Product
from api.serializers import ProductSerializer
from api.permissions import IsOddProductID, IsNotHacker      # classes taken from permissions.py


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get_permissions(self):
        """
            Question: IsAuthenticated applies to everything?
            
            Instantiates and returns the list of permissions that this view requires.
        """
        permission_objects = [IsAuthenticated(), IsNotHacker()]
        
        if self.action in ['create', 'update', 'partial_update', 'delete']:    # why use destroy originally?
            permission_objects += [IsAdminUser()]
        #elif self.action == 'retrieve':                  # get and retrieve are equivalent?
        else:
            permission_objects += [IsOddProductID()]  # I was missing this check
        
        return permission_objects
    
#     def get_permissions(self):
#         """
#         Instantiates and returns the list of permissions that this view requires.
#         """
#         # permissions that apply to everyone
#         permission_classes = [IsAuthenticated, IsNotHacker]
        
#         actions = ['create', 'update', 'partial_update', 'delete']
        
#         if self.action in actions:
#             permission_classes += [IsAdminUser] # not IsAdmin?
#         else:
#             permission_classes += [IsAuthenticated] # for everyone else
#         return [permission() for permission in permission_classes]

#                 # return list of each object!
    
##### Define here the permissions for each endpoints according to the
    # following conditions:

    # - All endpoints will require the user to be authenticated
    #   (see `IsAuthenticated` permission from DRF) and not being a hacker
    #   (see `IsNotHacker` permission inside `api/permissions.py`)

    # - All endpoints that modify the database will require the user to be admin
    #   (see `IsAdminUser` permission from DRF).
    #   This endpoints are the create, update, partial update and delete.

    # - The retrieve endpoint will need the user to pass the `IsOddProductID`
    #   permission (must also be implemented inside `api/permissions.py`)
    
    # need to add the access, permissions list = function get_permissions that returns a list
    
#### From README.md    

# - All endpoints that modify the database will require the user to be admin (see `IsAdminUser` permission from DRF). This endpoints are the create, update, partial update and delete.

    
# NOTE ABOUT SETTINGS.PY:
#
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         ### YOUR CODE HERE
#     ),
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 3
# }
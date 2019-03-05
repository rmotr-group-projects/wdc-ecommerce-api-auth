from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.models import Product
from api.serializers import ProductSerializer
from api.permissions import IsOddProductID, IsNotHacker


class ProductViewSet(viewsets.ModelViewSet):    # ModelViewSet creates all views for the model with post, get, delete, etc.... All views are API endpoints.
    serializer_class = ProductSerializer        # JsonResponse() to Product
    queryset = Product.objects.all()    # DRF knows to .get() a list or detail view
					                    # Do .all() as standard, but, you can .filter() this etc.

    # Define here the permissions for each endpoints according to the
    # following conditions:

    # - All endpoints will require the user to be authenticated
    #   (see `IsAuthenticated` permission from DRF) and not being a hacker
    #   (see `IsNotHacker` permission inside `api/permissions.py`)

    # - All endpoints that modify the database will require the user to be admin
    #   (see `IsAdminUser` permission from DRF).
    #   This endpoints are the create, update, partial update and delete.

    # - The retrieve endpoint will need the user to pass the `IsOddProductID`
    #   permission (must also be implemented inside `api/permissions.py`)

    def get_permissions(self):
        permissions = [IsAuthenticated(), IsNotHacker()]
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions += [IsAdminUser()]
        elif self.action == 'retrieve':
            permissions += [IsOddProductID()]
        return permissions

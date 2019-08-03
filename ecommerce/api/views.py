from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.models import Product
from api.serializers import ProductSerializer
from api.permissions import IsOddProductID, IsNotHacker


class ProductViewSet(viewsets.ModelViewSet):
    #ModelVieweSet just need serializer and queryset
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    #Limit actions on view set based on permissions
    def get_permissions(self):
        #Checks if user is not 'hacker'
        permissions = [IsAuthenticated(), IsNotHacker()]
        #To perform create,update,partial_update,destroy user needs to be AdminUser
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions += [IsAdminUser()]
        #If you want to retrieve specific objects needs to Pass IsOddProductID    
        elif self.action == 'retrieve':
            permissions += [IsOddProductID()]
        return permissions
        
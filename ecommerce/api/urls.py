from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('products', views.ProductViewSet, base_name='products')  # products/    and     products/1 , etc

urlpatterns = [url for url in router.urls]
# OR do -->  # urlpatterns += router.urls

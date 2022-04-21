from rest_framework import routers, viewsets
from rest_framework.decorators import api_view

from FazlaGidaChallenge.models import Product, Store
from .serializers import ProductFavoriteSerializer, StoreFavoriteSerializer


@api_view(["GET"])
def get_favorite(request):
    if request.method == "GET":
        pass


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFavoriteSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreFavoriteSerializer


def create_router() -> routers.BaseRouter:
    router = routers.DefaultRouter()
    router.register(r"api/products", ProductViewSet)
    router.register(r"api/stores", StoreViewSet)
    return router

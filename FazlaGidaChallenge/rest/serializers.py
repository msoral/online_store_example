from rest_framework import serializers

from FazlaGidaChallenge.models import Product, Store


class ProductFavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "price",
            "category",
            "store",
            "favorite",
        )


class StoreFavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name", "slug", "favorite")

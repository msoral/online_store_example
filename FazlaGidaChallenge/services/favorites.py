from typing import Iterable

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from ..interfaces import Favoritable
from ..models import Product, Store


def toggle_product_favorite(ide, user: User) -> None:
    product = get_object_or_404(Product, id=ide)
    if product.is_favorite(user.id):
        product.favorite.remove(user)
    else:
        product.favorite.add(user)


def add_store_to_favorites(ide, user: User) -> Store:
    store = get_object_or_404(Store, id=ide)
    if store.is_favorite(user.id):
        store.favorite.remove(user)
    else:
        store.favorite.add(user)
    return store


def get_favorites(
    model_list: Iterable[Favoritable], user_id: int
) -> dict[Favoritable, bool]:
    return dict(
        zip(model_list, map(lambda product: product.is_favorite(user_id), model_list))
    )


def get_user_favorites(user_id: int) -> dict[str, dict[Favoritable, bool]]:
    products = Product.objects.all()
    products = get_favorites(products, user_id)
    stores = Store.objects.all()
    stores = get_favorites(stores, user_id)
    return {"products": products, "stores": stores}

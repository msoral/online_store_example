from django.shortcuts import render, get_object_or_404, redirect

from FazlaGidaChallenge.models import Product, Store
from FazlaGidaChallenge.services.favorites import get_favorites, add_store_to_favorites


def store(request):
    stores = Store.objects.all()
    return render(request, "store.html", {"stores": stores})


def store_detail(request, slug):
    a_store: Store = get_object_or_404(Store, slug=slug)
    products = Product.objects.filter(store=a_store)
    favorites = get_favorites(products, request.user.id)

    context = {"store": a_store, "products": products, "favorites": favorites}
    return render(request, "store_detail.html", context)


def favorite_store(request, ide):
    add_store_to_favorites(ide, request.user)
    return redirect(store)

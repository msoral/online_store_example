from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from FazlaGidaChallenge.models import Product, Store
from FazlaGidaChallenge.services.favorites import get_favorites, toggle_store_favorite


def store(request):
    stores = Store.objects.all()
    stores = get_favorites(stores, request.user.id)
    return render(request, "store.html", {"stores": stores})


def store_detail(request, slug):
    a_store: Store = get_object_or_404(Store, slug=slug)
    products = Product.objects.filter(store=a_store)
    products = get_favorites(products, request.user.id)
    is_favorite = a_store.is_favorite(request.user.id)

    context = {
        "store": a_store,
        "products": products,
        "is_favorite": is_favorite
    }

    return render(request, "store_detail.html", context)


def favorite_store(request, ide):
    toggle_store_favorite(ide, request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

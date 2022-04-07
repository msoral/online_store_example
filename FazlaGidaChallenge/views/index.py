from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template.defaultfilters import register

from FazlaGidaChallenge.interfaces import Favoritable
from FazlaGidaChallenge.models import Category, Product
from FazlaGidaChallenge.services.favorites import (
    add_product_to_favorites,
    get_favorites,
)


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get("category", "")

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get("query", "")
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    favorites = get_favorites(products, request.user.id)

    context = {
        "categories": categories,
        "products": products,
        "active_category": active_category,
        "favorites": favorites,
    }
    return render(request, "index.html", context)


@login_required
def favorite_product(request, ide):
    add_product_to_favorites(ide, request.user)
    return redirect(index)


@register.filter
def get_item(dictionary: dict[Favoritable, bool], key) -> bool:
    if dictionary:
        return dictionary.get(key)
    else:
        return False

from django.shortcuts import render, get_object_or_404

from ..models import Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    is_favorite = product.is_favorite(request.user.id)
    context = {
        "product": product,
        "is_favorite": is_favorite,
    }
    return render(request, "product_detail.html", context)

from django.shortcuts import render, get_object_or_404, redirect

from ..forms import AddProductForm
from ..models import Product
from ..services.product import ProductService


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    is_favorite = product.is_favorite(request.user.id)
    context = {
        "product": product,
        "is_favorite": is_favorite,
    }
    return render(request, "product_detail.html", context)


def add_product(request):
    # TODO: Find why html is not connected to this view function.
    if request.method == "POST":
        form = AddProductForm(request.POST)

        if form.is_valid():
            product = form.save()

            ProductService.add(product)
            redirect(request.path)
    else:
        form = AddProductForm()
    return render(request, "components/add_product.html", {"form": form})

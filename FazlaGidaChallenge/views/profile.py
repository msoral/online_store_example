from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile
from ..services.favorites import get_user_favorites, toggle_product_favorite


@login_required
def profile(request):
    a_profile = Profile.objects.get_or_create(user=request.user)
    favorites = get_user_favorites(request.user.id)

    context = {
        "profile": a_profile,
        "products": favorites["products"],
        "stores": favorites["stores"],

    }
    return render(request, "profile.html", context)

@login_required
def favorite_product(request, ide):
    toggle_product_favorite(ide, request.user)
    return redirect(profile)

@login_required
def edit_profile(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.username = request.POST.get("username")
        user.save()

        return redirect("profile")
    return render(request, "edit_profile.html")

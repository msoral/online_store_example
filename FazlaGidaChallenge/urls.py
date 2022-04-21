from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from . import rest

router = rest.create_router()

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path("stores/", views.store, name="store"),
    path("stores/<slug:slug>", views.store_detail, name="store_detail"),
    path("products/add", views.add_product, name="add_product"),
    path("products/<slug:slug>", views.product_detail, name="product"),
    path("profile/", views.profile, name="profile"),
    path(
        "product/favorites/<int:ide>/",
        views.favorite_product,
        name="add_favorite_product",
    ),
    path("store/favorites/<int:ide>", views.favorite_store, name="add_favorite_store"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]

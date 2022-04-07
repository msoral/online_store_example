from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .category import Category
from .store import Store


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=600, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=datetime.now())
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name="favorite_product", blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

    def is_favorite(self, user_id):
        return self.favorite.filter(id=user_id).exists()

    def get_user_favorites(self, user_id):
        return self.favorite.filter(user_id=user_id)

    def get_favorites(self):
        return self.favorite.all()

from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    favorite = models.ManyToManyField(User, related_name="favorite_store", blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def is_favorite(self, user_id):
        return self.favorite.filter(id=user_id).exists()

    def get_user_favorites(self, user_id):
        return self.favorite.filter(user_id=user_id)

    def get_favorites(self):
        return self.favorite.all()

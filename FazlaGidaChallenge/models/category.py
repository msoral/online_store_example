from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    class Meta:
        unique_together = ("name",)

    def get_or_create(self) -> tuple[models.Model, bool]:
        return self.objects.get_or_create(self.name)

    def __create_slug(self):
        words = self.name.lower().split(" ")
        return "_".join(words)

    def __str__(self):
        return self.name

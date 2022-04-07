from FazlaGidaChallenge.models import Category


def create_new_category(name: str) -> None:
    category = Category(name)
    category.save()


def get_category(name: str) -> Category:
    return Category.objects.get(name)

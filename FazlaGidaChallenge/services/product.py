from FazlaGidaChallenge.models import Product


class ProductService:

    @staticmethod
    def add(product: Product):
        product.save()

    @staticmethod
    def remove(product_id: int):
        product: Product = Product.objects.get(product_id)
        product.delete()

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

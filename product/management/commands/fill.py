# myapp/management/commands/fill.py
from django.core.management import BaseCommand
from product.models import Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Яблоко', 'description': 'желтые', 'category': 'Фрукты', 'price': '10', 'date_create': '2020-01-17 16:50', 'date_change': '2021-04-17 12:50', 'picture': 'Яблоки.jpg'},
            {'name': 'Огурец', 'description': 'зеленые', 'category': 'Овощи', 'price': '11', 'date_create': '2020-01-17 16:51', 'date_change': '2022-04-17 13:50', 'picture': 'Огурцы.jpeg' },
            {'name': 'Помидор', 'description': 'красный', 'category': 'Овощи', 'price': '12', 'date_create': '2020-01-17 16:52', 'date_change': '2023-04-17 17:50', 'picture': 'Помидоры.jpg'},
            {'name': 'Апельсин', 'description': 'оражжевый', 'category': 'Фрукты', 'price': '13', 'date_create': '2020-01-17 16:53', 'date_change': '2021-03-17 16:50', 'picture': 'Апельсины.jpg'},
            {'name': 'Фундук', 'description': 'круглый', 'category': 'Орехи', 'price': '14', 'date_create': '2020-01-17 16:54', 'date_change': '2023-08-17 16:50', 'picture': 'фундук_очищеный_сырой.jpg' },
            {'name': 'Арахис', 'description': 'соленый', 'category': 'Орехи', 'price': '15', 'date_create': '2020-01-17 16:55', 'date_change': '2022-12-17 16:50', 'picture': 'арахис.png'},
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
                )
        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_create)

# Your_model.objects.all().delete()
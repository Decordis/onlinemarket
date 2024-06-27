from django_filters import FilterSet
from .models import Product

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.

class ProductFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # Указываем по каким поля идет фильтрация
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': [
                'lt', #цена должна быть меньше/равна указанной
                'gt', #здесь наоборот больше/равно указанной
            ]
        }
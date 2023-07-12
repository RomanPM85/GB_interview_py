from django.urls import path
# from homework.homework.products.product_app.views import index, add
from product_app.views import index, add

app_name = 'product_app'

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
]


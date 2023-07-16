from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from product_app.forms import ProductForm
from product_app.models import Product
# from homework.homework.products.product_app.forms import ProductForm
# from homework.homework.products.product_app.models import Product

def index(request):
    return render(request, 'product/index.html', {'product': Product.objects.all()})


def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    return render(request, 'product/form.html', {'form': form})

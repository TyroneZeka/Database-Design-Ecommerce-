from django.db.models.aggregates import Count
from django.shortcuts import render
from inventory.models import *


def home(request):
    data = Category.objects.all()
    return render(request, "index.html", {"data": data})


def category(request):
    data = Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):
    data = Product.objects.filter(category__name=category).values(
        "id",
        "name",
        "slug",
        "product__store_price",
        "product__product_inventory__units",
    )
    return render(
        request, "product_by_category.html", {"data": data}
    )


def product_detail(request, slug):

    filter_arguments = []
    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)


    data = ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in = filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments)).values("id","sku","store_price","product_inventory__units","product__name")

    return render(request, "product_detail.html", {"data": data})

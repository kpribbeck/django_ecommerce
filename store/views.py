from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Category, Product, ProductVariant

def index(request):
    biggest_products = ProductVariant.objects.order_by("size")[:3].select_related('product')
    # template = loader.get_template("store/index.html")
    context = {"biggest_products": biggest_products}
    output = ", ".join([p.product.name for p in biggest_products])
    # return HttpResponse(template.render(context, request))
    return render(request, "store/index.html", context)
    #return HttpResponse(output)

def getProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # try:
    #     product_variant = ProductVariant.objects.filter(id=product_id)
    # except ProductVariant.DoesNotExist:
    #     raise Http404("Product does not exist")

    return render(request, "store/product.html", {"product": product})

def getVariant(request, product_variant_id):
    product_variant = get_object_or_404(ProductVariant, id=product_variant_id)
    # try:
    #     product_variant = ProductVariant.objects.filter(id=productVariant_id)
    # except ProductVariant.DoesNotExist:
    #     raise Http404("Product does not exist")

    return render(request, "store/productVariant.html", {"product_variant": product_variant})


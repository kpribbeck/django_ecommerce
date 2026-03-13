from django.urls import path

from . import views

app_name = "store"
urlpatterns = [
    path("", views.index, name = "index"),
    path("product/<int:product_id>", views.getProduct, name = "product"),
    path("product/variant/<int:productVariant_id>", views.getVariant, name="getVariant"),
]
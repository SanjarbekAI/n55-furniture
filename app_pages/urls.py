from django.urls import path

from app_pages.views import HomeTemplateView, ProductsTemplateView

app_name = "pages"

urlpatterns = [
    path('products/', ProductsTemplateView.as_view(), name='products'),
    path('', HomeTemplateView.as_view(), name='home'),
]

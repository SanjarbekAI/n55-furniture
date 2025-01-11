from django.urls import path

from app_pages.views import HomeTemplateView, BlogsTemplateView, ProductsTemplateView

app_name = "pages"

urlpatterns = [
    path('blogs/', BlogsTemplateView.as_view(), name='blogs'),
    path('products/', ProductsTemplateView.as_view(), name='products'),
    path('', HomeTemplateView.as_view(), name='home'),
]

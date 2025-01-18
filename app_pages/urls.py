from django.urls import path

from app_pages.views import HomeTemplateView, ProductsTemplateView, ContactCreateView

app_name = "pages"

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductsTemplateView.as_view(), name='products'),
    path('', HomeTemplateView.as_view(), name='home'),
]

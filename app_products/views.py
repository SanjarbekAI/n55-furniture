from django.views.generic import TemplateView


class ProductDetailView(TemplateView):
    template_name = 'shop/product-detail.html'


class ProductListView(TemplateView):
    template_name = 'shop/products-list.html'

from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class ProductsTemplateView(TemplateView):
    template_name = 'shop/products-list.html'

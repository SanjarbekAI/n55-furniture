from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class BlogsTemplateView(TemplateView):
    template_name = 'blogs/blog-list.html'

class ProductsTemplateView(TemplateView):
    template_name = 'shop/products-list.html'

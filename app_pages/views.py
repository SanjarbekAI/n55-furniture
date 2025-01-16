from django.views.generic import TemplateView, ListView

from app_blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class BlogsTemplateView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = "blogs"

    def get_queryset(self):
        blogs = BlogModel.objects.all()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        if tag:
            blogs = blogs.filter(tags=tag)
        if category:
            blogs = blogs.filter(categories=category)

        return blogs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = BlogCategoryModel.objects.all()
        context["recent_blogs"] = BlogModel.objects.order_by('-created_at')[:2]
        context["tags"] = BlogTagModel.objects.all()
        return context


class ProductsTemplateView(TemplateView):
    template_name = 'shop/products-list.html'

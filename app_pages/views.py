from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.utils.translation import gettext_lazy as _

from app_pages.forms import ContactModelForm
from app_pages.models import ContactModel


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'


class ProductsTemplateView(TemplateView):
    template_name = 'shop/products-list.html'


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    model = ContactModel
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form):
        messages.success(self.request, _("Your contact information is successfully sent"))
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors:
            messages.error(self.request, error)
        return super().form_invalid(form)


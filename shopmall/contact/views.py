from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm


class ContactView(FormView):
    template_name = "contacts/contact.html"
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

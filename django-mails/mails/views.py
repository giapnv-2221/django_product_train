from django.shortcuts import render
from django.core.mail import send_mail as sendmail
from django.conf import settings
from . import forms


def send_mail(request):
    if request.POST:
        form = forms.MailForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            message = form.cleaned_data["content"]
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data["email"], ]
            sendmail(title, message,  from_email, recipient_list)
            return render(request, "mail/new.html", {"form": form})
    form = forms.MailForm()

    return render(request, "mail/new.html", {"form": form})



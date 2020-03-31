from django import forms

class MailForm(forms.Form):
    email = forms.CharField()
    title = forms.CharField()
    content = forms.CharField()

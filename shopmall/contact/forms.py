from django import forms


class ContactForm(forms.Form):
    title = forms.CharField(max_length=60)
    content = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        print(self.cleaned_data)
        print("Sending mail!")

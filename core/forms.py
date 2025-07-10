from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        subject = f"Contact Form Submission from {self.cleaned_data['name']}"
        message = self.cleaned_data['message']
        email_from = self.cleaned_data['email']
        recipient_list = [settings.DEFAULT_FROM_EMAIL]

        send_mail(subject, message, email_from, recipient_list)


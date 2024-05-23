from django import forms
from django.core.mail import EmailMessage

from django.conf import settings


class ContactForm(forms.Form):
    Name = forms.CharField(
        max_length=254,
        required=True,
    )
    Email = forms.EmailField(
        max_length=254,
        required=True,
    )
    Subject = forms.CharField(
        max_length=254,
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )

    def send_mail(self):
        if self.is_valid():
            Name = self.cleaned_data['Name']
            Email = self.cleaned_data['Email']
            Subject = self.cleaned_data['Subject']
            message = self.cleaned_data['message']
            message_context = 'Message received.\n\n' \
                              'Name: %s\n' \
                              'Subject: %s\n' \
                              'Email: %s\n' \
                              'Message: %s' % (Name, Subject, Email, message)
            email = EmailMessage(
                Subject,
                message_context,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[Email],
            )
            email.send()

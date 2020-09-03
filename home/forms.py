from django import forms
from django.forms import ModelForm
from home.models import Contact


class ContactForm(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 's6-name c-forms', "placeholder": "Name"}), label='')

    email = forms.CharField(widget=forms.EmailInput
                            (attrs={'class': 's6-email c-forms',
                                    "placeholder": "Your Email"
                                    }), label='')

    message = forms.CharField(widget=forms.Textarea
                              (attrs={'class': 's6-message c-forms',
                                      "placeholder": "Message"
                                      }), label='')

    class Meta:
        model = Contact
        fields = "__all__"

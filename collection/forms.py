from django.forms import ModelForm
from django import forms
from collection.models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "your email:"
        self.fields['content'].label = "What do you want to say?"

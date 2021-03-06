from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from collection.models import Thing, Upload

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

class ThingUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('image',)

class EditEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)

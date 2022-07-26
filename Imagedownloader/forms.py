from pyexpat import model
from django import forms
from .models import image 
from urllib import request
from django.core.files.base import Contentfile
from django.utils.text import slugify

class ImageCreatedForm(forms.ModelForm):
    class Meta:
        model = image
        wigdets = {
            'url':forms.HiddenInput(),
        }
        fields = ('title', 'url', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extension = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension in valid_extension:
            raise forms.ValidationError('given url does not support image ext')

    def save(self, force_insert=False,force_update=False,commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image name = f'{name},{extension}'

        #download image from  given url
        response = request.urlopen(image_url)
        image.image.save(image_name, Contentfile(response.read()), save=False)
        if commit:
            image.save()
        return image

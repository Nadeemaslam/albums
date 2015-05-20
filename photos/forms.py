from django.forms import ModelForm
from photos.models import Picture

class PictureForm(ModelForm):
    class Meta:
       model = Picture
       fields = ['author','gallery_name','title', 'description','created','pic']
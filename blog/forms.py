from django.forms import ModelForm

from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title']
        # fields = '__all__' # documentation doesn't recommend this
        # exclude = [title] # if you want to exclude a particular field from the form
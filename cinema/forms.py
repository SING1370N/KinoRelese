from django import forms
from django.forms import modelformset_factory, inlineformset_factory

from .models import Film, Hall, Cinema
from gallery_seo.models import Image_gallery, SEO
from gallery_seo.forms import SeoForm, GalleryForm


class FilmForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    trailer_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    gallery = GalleryForm()

    class Meta:
        model = Film
        fields = ['type_IMAX', 'type_3D', 'type_2D', 'description', 'name', 'trailer_url', 'date', 'main_image']
        # fields = '__all__'


class HallForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id', 'width': '30%'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    class Meta:
        model = Hall
        fields = ['name', 'description', 'scheme', 'banner_image']


class CinemaForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_id'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    conditions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cinema
        fields = ['logo', 'banner_image', 'name', 'description', 'conditions', 'phone', 'email']


HallFormSet = modelformset_factory(Hall, form=HallForm, can_delete=True)

from django import forms
from .models import Product, Category, Genre
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        genres = Genre.objects.all()
        genre_friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['genre'].choices = genre_friendly_names
        self.fields['genre'].empty_label = "Null"
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

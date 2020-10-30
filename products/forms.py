from django import forms
from .models import Wine, WineType


class ProductForm(forms.ModelForm):

    class Meta:
        model = Wine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        wine_types = WineType.objects.all()
        friendly_names = [(w.id, w.get_friendly_name()) for w in wine_types]

        self.fields['wine_type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

from django import forms

from product.config import prohibited_products
from product.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('user_own',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data.lower() in prohibited_products:
            raise forms.ValidationError('В названии присутствует запрещенное слово')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    # def clean_is_relevant(self):
    #     cleaned_data = self.cleaned_data['is_relevant']
    #     for version_is_relevant in
    #         print(version_is_relevant)
    #         raise forms.ValidationError('Может быть активна только одна версия')
    #     return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_relevant':
                field.widget.attrs['class'] = 'form-control'

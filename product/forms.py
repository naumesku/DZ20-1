from django import forms
from product.models import Product, Version


class ProductForm(forms.ModelForm):

    prohibited_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data.lower() in self.prohibited_products:
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
    #     if cleaned_data == True:
    #         if Version.objects.filter(is_relevant=True).first():
    #             return cleaned_data
    #     raise forms.ValidationError('Может присутствовать только одна активная версия')
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form'
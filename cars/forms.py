from django import forms
from cars.models import Car #Brand  

# Método antigo 
'''
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'], # Self se refere -> CarForm
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
'''
# Método mais eficaz 
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__' # Busca totas as yabrlas do DB disponiveis 
    
    def clean_value(self): # self -> é formulario que está chegando aqui
        value = self.cleaned_data.get('value')
        if value < 15000:
            self.add_error('value', 'Valor minimo de carro deve ser de R$ 15.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1960:
            self.add_error('factory_year', 'Não é possivel cadastrar carros fabrigados antes de 1960')
        return  factory_year
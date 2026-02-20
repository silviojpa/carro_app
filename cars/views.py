# from django.shortcuts import render, redirect -> menos convencional
from cars.models import Car
from cars.forms import CarModelForm  # CarForm -> importação do método antigo do arquivo forms.py
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.http import HttpResponse
# from django.views import View -> menos convencional
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Novo View da função car_view 
    
class CarsListView(ListView): # Listagem dos carros
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    
@method_decorator(login_required(login_url='login'), name='dispatch') # Camada de segurança que verifica o login antes de acessar a class 
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
     model = Car
     form_class = CarModelForm
     template_name = 'car_update.html'
     success_url = '/cars/'
     def get_success_url(self):
         return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
     

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

# Class menos convencional, sendo trocado pela Class CreateView
'''
class NewCarView(View):
    
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
'''

# Funçao OLD View
'''
class CarsView(View): # Herda todas as função da View

    def get(self, request):
        cars = Car.objects.all().order_by('model') 
        search = request.GET.get('search')

        if search:
            cars = Car.objects.filter(model__icontains=search)  
        return render(
        request, 
        'cars.html',
        {'cars': cars}
        ) 

---------------------------------------------------------------------------------
'''
# Funçao menos convencional
'''
# Funçao OLD -> def cars_view(request):
def cars_view(request):
    cars = Car.objects.all().order_by('model') # Quary Set do BD
    search = request.GET.get('search')

    if search: # Caso user faça uma busca pelo ?search=string
        cars = Car.objects.filter(model__icontains=search)# .order_by('model') # Traz todos os registros do banco de dados  
# filter -> filtra pelo um dado dentro do DB
# icontains -:> ignora se o user usa caixa alta ou baixa
    return render(
        request, 
        'cars.html',
        {'cars': cars}
        ) 
# # render -> rederiza uma resposta em http e devolve uma response em http para user
# return HttpResponse(html) # HTML dentro da função.
'''

# Função OLD -> def new_car_view(request):
'''
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES) # pegando os dados do cliente
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})
'''
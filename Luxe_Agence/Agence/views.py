from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import ResidenceRegistration
from .models import Residence

# def home(request):
#     return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


# Create your views here.

# fonction pour afficher des infos
def list_residences(request):
    residences = Residence.objects.all()
    return render(request, 'home.html', {'residences': residences})

# fonction pour ajouter et afficher infos
def add_residence(request):
    if request.method == 'POST':
        form = ResidenceRegistration(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Résidence ajoutée avec succès!")  # Ajoutez un message de débogage
            return redirect('home')
        else:
            print("Le formulaire n'est pas valide:", form.errors)  # Ajoutez un message de débogage en cas d'erreur
    else:
        form = ResidenceRegistration()
    return render(request, 'add.html', {'form': form})

# fonction pour modifier infos
def update_data(request, id):
    if request.method == 'POST':
        obj = Residence.objects.get(pk=id)
        fm = ResidenceRegistration(request.POST, instance = obj)
        if fm.is_valid():
            fm.save()
    else:
        obj = Residence.objects.get(pk=id)
        fm = ResidenceRegistration(instance = obj)
    return render(request, 'update.html',{'form': fm})

# fonction pour supprimer infos

def delete_data(request, id):
    if request.method == 'POST':
        obj= Residence.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect('/')
        




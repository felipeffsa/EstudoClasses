from django.shortcuts import render
from django.views.generic import ListView
from usuario.models import Pessoas

# Create your views here.
class PessoasListView(ListView):
    model = Pessoas
    template_name ='home.html'
    context_object_name ='pessoas' #Esse é o nosso contexto
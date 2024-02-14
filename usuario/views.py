from django.shortcuts import render
from django.views.generic import ListView,DetailView
from usuario.models import Pessoas

# Create your views here.
class PessoasListView(ListView):
    model = Pessoas
    template_name ='home.html'
    context_object_name ='pessoas' #Esse é o nosso contexto



class PessoasDetailView(DetailView):
    model = Pessoas
    template_name ='detalhes.html'
    context_object_name ='detail'
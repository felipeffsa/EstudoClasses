from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from usuario.models import Pessoas
from django.urls import reverse_lazy
# Create your views here.
class PessoasListView(ListView):
    model = Pessoas
    template_name ='home.html'
    context_object_name ='pessoas' #Esse é o nosso contexto



class PessoasDetailView(DetailView):
    model = Pessoas
    template_name ='detalhes.html'
    context_object_name ='detail'
    
# Classe para criação de cadastro
class CriarVisu(CreateView): # Essa é uma view utilizada para criar uma nova pessoa no cadastro. Ela deve herdar de CreateView.
    model = Pessoas  # Passamos a classe na qual queremos criar um novo cadastro.
    fields = ['nome','idade','nacionalidade','profissao'] # Aqui será passado os campos que nós queremos que apareça no formulário.
    template_name = 'criar.html' # O template contendo o formulário com o metodo POST.
    success_url = '/pessoas/' # A url que será redirecionada, quando acontecer o POST.
    def form_valid(self,form): # Essa função irá verificar se o formulario é valido. Ela é semelhante a do ModelForm. 'form.is_valid()'.
        return super().form_valid(form) # Utilizamos o 'super()' para pegar a função da classe pai.
                                        # Classe para a atualização do cadastro

class AtualizarCadastro(UpdateView):
    model = Pessoas
    fields = ['nome','idade','nacionalidade','profissao']
    template_name ='atualizar.html'
    success_url ='/pessoas/'


class DeletarCadastro(DeleteView):
    model = Pessoas
    template_name = 'deletar.html'
    success_url = reverse_lazy('pessoas')
    
    
from django.urls import path
from usuario.views import PessoasListView,PessoasDetailView,CriarVisu,AtualizarCadastro,DeletarCadastro


urlpatterns = [
    path('pessoas/',PessoasListView.as_view(), name ='pessoas'),
    path('detalhes/<int:pk>/',PessoasDetailView.as_view(), name ='detail'),
    path('criar/',CriarVisu.as_view(), name ='criar'),
    path('atualizar/<int:pk>/',AtualizarCadastro.as_view(),name ='atualizar' ),
    path('deletar/<int:pk>/',DeletarCadastro.as_view(), name ='deletar')
]
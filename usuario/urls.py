from django.urls import path
from usuario.views import PessoasListView,PessoasDetailView


urlpatterns = [
    path('pessoas/',PessoasListView.as_view(), name ='pessoas'),
    path('detalhes/<int:pk>/',PessoasDetailView.as_view(), name ='detail')
]
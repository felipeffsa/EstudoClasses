from django.urls import path
from usuario.views import PessoasListView


urlpatterns = [
    path('pessoas/',PessoasListView.as_view(), name ='pessoas')
]
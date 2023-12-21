from django.urls import path
from .views import cadastrar, listar, detalhar, atualizar, deletar, cadastrar_cliente, listar_cliente, detalhar_cliente, atualizar_cliente, deletar_cliente

urlpatterns = [
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('', listar, name='listar'),
    path('detalhar/<int:id>/', detalhar, name='detalhar'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('deletar/<int:id>/', deletar, name='deletar'),

    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_cliente/', listar_cliente, name='listar_cliente'),
    path('detalhar_cliente/<int:id>/', detalhar_cliente, name='detalhar_cliente'),
    path('atualizar_cliente/<int:id>/', atualizar_cliente, name='atualizar_cliente'),
    path('deletar_cliente/<int:id>/', deletar_cliente, name='deletar_cliente'),
]
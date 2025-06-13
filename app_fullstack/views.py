from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuario = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuario)
# Create your views here.

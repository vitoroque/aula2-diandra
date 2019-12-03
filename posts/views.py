from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Gabriel'
    contexto = {
        'nome': nome
    }
    return render(request, 'home.html', contexto)
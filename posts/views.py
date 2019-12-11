from django.shortcuts import render
from .form import PedidoForm

# Create your views here.
def home(request):
    return render(request, 'home.html', contexto)

def post(request):
    return render(request, 'post.html')

def cadastro(request):
    forms = PedidoForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        context = {
            "msg" : "Pedido deu Certo!!"
        }
         return render(request, 'cadastro.html', context)

    context = {
        "formulario" : forms 
    }     
    return render(request, 'cadastro.html', context)
    
   
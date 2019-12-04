from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'groger'
    # posts = {
    #     'Gabriel' : 'Narnia para projetos ágeis',
    #     'Vinicius': 'IA para comer biscoitos',
    #     'Ana Lu': 'BTS é muito bondoso',
    #     'Downtown': 'Não seja maníaco'
    # }

    lista = ['Roré', 'Generro', 'Anlu', 'DOwnT0wn']
    contexto = {
        'nome': nome,
        'lista': lista
    }
    return render(request, 'home.html', contexto)
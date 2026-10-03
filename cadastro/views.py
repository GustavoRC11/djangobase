from django.shortcuts import render

def index(request):
    return render(request, 'cadastro/index.html')

def contato(request):
    return render(
        request,
        'cadastro/contato.html'
    )
def sobre(request):
    return render(
        request,
        'cadastro/sobre.html'

    )
from django.shortcuts import render, redirect
from .models import Pessoa

def home(request):
    pessoa = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoa})

def salvar(request):
    nomev = request.POST.get("nome")
    Pessoa.objects.create(nome=nomev)
    pessoa = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoa})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    nomev = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nomev
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
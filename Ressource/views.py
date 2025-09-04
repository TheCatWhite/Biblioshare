

from django.shortcuts import render,redirect

from Utilisateur.forms import RessourceForm
from .models import Ressource , Telechargement, Favori
from Utilisateur.forms import RessourceForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.db.models import Q



def liste_ressources(request):
    ressources = Ressource.objects.all().order_by("-date_ajout")
    return render(request, "ressource/liste.html", {"ressources": ressources})



@login_required
def upload_ressource(request):
    if request.method == "POST":
        form = RessourceForm(request.POST, request.FILES)
        if form.is_valid():
            ressource = form.save(commit=False)
            ressource.proprietaire = request.user
            ressource.save()
            return redirect("ressource:liste_ressources")
    else:
        form = RessourceForm()
    return render(request, "ressource/upload.html", {"form": form})

@login_required
def telecharger_ressource(request, pk):
    ressource = get_object_or_404(Ressource, pk=pk)
    Telechargement.objects.create(utilisateur=request.user, ressource=ressource)
    response = FileResponse(ressource.fichier.open('rb'), as_attachment=True, filename=ressource.fichier.name.split('/')[-1])
    return response





@login_required
def recherche_ressource(request):
    query = request.GET.get('q', '')
    ressources = []

    if query:
        ressources = Ressource.objects.filter(
            Q(titre__icontains=query) |
            Q(type__icontains=query) |
            Q(proprietaire__username__icontains=query)
        )

    return render(request, 'ressource/recherche_ressource.html', {
        'ressources': ressources,
        'query': query,
    })

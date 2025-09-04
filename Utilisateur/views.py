from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q
from Ressource.models import Ressource
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès ! Vous pouvez vous connecter.")
            return redirect('utilisateur:connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('utilisateur:profil')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'auth/connexion.html')


@login_required
def profil(request):
    return render(request, 'user/profil.html')


@login_required
def deconnexion(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect('utilisateur:connexion')


@login_required
def modifier_profil(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour avec succès ✅")
            return redirect("utilisateur:profil")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "user/modifier_profil.html", {"form": form})




@login_required
def modifier_mot_de_passe(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save() 
            update_session_auth_hash(request, user)  
            messages.success(request, "Mot de passe modifié avec succès 🔑")
            return redirect("utilisateur:profil")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "user/modifier_mot_de_passe.html", {"form": form})


User = get_user_model()

@login_required
def recherche_utilisateur(request):
    query = request.GET.get('q', '')
    utilisateurs = []

    if query:
        utilisateurs = User.objects.filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )

    return render(request, 'user/recherche.html', {
        'utilisateurs': utilisateurs,
        'query': query
    })

@login_required
def profil_utilisateur(request, user_id):
    utilisateur = get_object_or_404(User, id=user_id)
    ressources = utilisateur.ressources.all().order_by('-date_ajout')  
    return render(request, 'user/profil_utilisateur.html', {
        'utilisateur': utilisateur,
        'ressources': ressources
    })

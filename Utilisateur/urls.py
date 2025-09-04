from django.contrib import admin
from django.urls import path
from Utilisateur import views
app_name = "utilisateur"
urlpatterns = [
    path('',views.inscription, name='inscription'),
    path('connexion/',views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
    path("profil/modifier/", views.modifier_profil, name="modifier_profil"),
    path("profil/motdepasse/", views.modifier_mot_de_passe, name="modifier_mot_de_passe"),
#    path('recherche/', views.recherche_utilisateur, name='recherche_utilisateur'),
    path('profil/<int:user_id>/', views.profil_utilisateur, name='profil_utilisateur'),

]

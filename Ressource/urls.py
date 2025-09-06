from django.urls import path
from . import views
app_name = "ressource"
urlpatterns = [
    path("listes/", views.liste_ressources, name="liste_ressources"),
    path("upload/", views.upload_ressource, name="upload_ressource"),
    path('telecharger/<int:pk>/', views.telecharger_ressource, name='telecharger_ressource'),
    path('recherche_ressource/', views.recherche_ressource, name='recherche_ressource'),
    path('acceuil/', views.accueil, name='accueil'),
    path('mes-ressources-partagees/', views.mes_ressources_partagees, name='mes_ressources_partagees'),
    path('telechargements/',views.mes_ressources_telechargees,name="mes_ressources_telechargees"),
]

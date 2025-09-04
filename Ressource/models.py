from django.db import models
from django.conf import settings  # <-- utiliser le user défini dans AUTH_USER_MODEL

class Ressource(models.Model):

    TYPE_CHOICES = [
        ('cours', 'Cours'),
        ('sujet', 'Sujet'),
        ('correction', 'Correction'),
        ('tuto', 'Tutoriel'),
        ('livre', 'Livre'),
    ]

    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to="ressources/")  
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)
    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ressources")
    # <-- ici, on prend le modèle utilisateur défini dans settings

    def __str__(self):
        return f"{self.titre} ({self.type})"


class Telechargement(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="telechargements")
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE, related_name="telechargements")
    date_telechargement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} a téléchargé {self.ressource.titre}"


class Favori(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favoris")
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE, related_name="favoris")
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'ressource')

    def __str__(self):
        return f"{self.utilisateur.username} a mis en favori {self.ressource.titre}"

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # <-- important
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('Utilisateur.urls')),
    path('', include('Ressource.urls')),
)


# Gestion des fichiers médias en mode debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

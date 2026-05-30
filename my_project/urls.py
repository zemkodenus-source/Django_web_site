from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

# for translater
from django.conf.urls.i18n import i18n_patterns
import django.conf.urls.i18n as i18n

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    ]

# translated pages
urlpatterns += i18n_patterns(
path('', include('main.urls')),
    path('accounts/', include('users.urls')),
    path('links/' ,include('links_app.urls'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# Local
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_views.posts_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

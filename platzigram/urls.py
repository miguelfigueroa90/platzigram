# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# Local
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_views.posts_list, name='feed'),
    path('users/login/', users_views.login_form, name='login_form'),
    path('users/authenticate/', users_views.login_authenticate, name='login_authenticate'),
    path('users/logout/', users_views.logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

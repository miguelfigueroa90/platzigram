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
    path('users/login_authenticate/', users_views.login_authenticate, name='login_authenticate'),
    path('users/logout/', users_views.logout_user, name='logout'),
    path('users/signup/', users_views.signup_form, name='signup'),
    path('users/signup_user/', users_views.signup_user, name='signup_user'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

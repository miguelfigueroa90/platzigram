from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('id', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    search_fields = (
        'user__username', 
        'user__email', 
        'user__first_name', 
        'user__last_name', 
        'phone_number'
    )

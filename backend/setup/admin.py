from django.contrib import admin
from .models import CustomUser, ExtraHour, ExtraHourHistory

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(ExtraHour)
admin.site.register(ExtraHourHistory)
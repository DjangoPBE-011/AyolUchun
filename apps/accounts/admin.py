from django.contrib import admin
from apps.accounts.models import CustomUser, Interest, UserInterest, PromoCode

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
   

@admin.register(UserInterest)
class UserInterestAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
   


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
   list_display = ('code',)
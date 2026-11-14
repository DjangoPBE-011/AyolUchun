from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.accounts.choices import DeletedReason
from apps.base.models import media_upload_to,BaseModel
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,verbose_name=_("Email"))
    phone_number = models.CharField(max_length=20, blank=True,verbose_name=_("Phone Number"))
    bio = models.TextField(max_length=200, blank=True,verbose_name=_("Bio"))
    image = models.ImageField(upload_to=media_upload_to, blank=True, null=True,verbose_name=_("Profile Image"))
    deleted_reason = models.TextField(max_length=200, choices=DeletedReason.choices, blank=True, null=True, default=DeletedReason.I_THOUGHT_ABOUT_IT, verbose_name=_("Deleted Reason"))
    
    
    USERNAME_FIELD = 'email'        # Tizimga kirish (login) uchun emaildan foydalanadi
    REQUIRED_FIELDS = ['username']  # Superuser yaratishda majburiy so'raladigan qo'shimcha maydon
    
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
        
    def __str__(self):
        return self.username



class Interest(BaseModel):
    user = models.ManyToManyField(CustomUser, related_name='user_interests',verbose_name=_("User"))
    name = models.CharField(max_length=100, unique=True,verbose_name=_("Interest Name"))
    
    class Meta:
        verbose_name = _("Interest")
        verbose_name_plural = _("Interests")
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
        
        
        
class UserInterest(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='interests',verbose_name=_("User"))
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name='user_interests',verbose_name=_("Interest"))
    
    
    class Meta:
        verbose_name = _("User Interest")
        verbose_name_plural = _("User Interests")
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user.username} - {self.interest.name}"




class PromoCode(BaseModel):
    code = models.CharField(max_length=50, unique=True,verbose_name=_("code"))
    description = models.TextField(max_length=200, blank=True,verbose_name=_("Description"))
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2,verbose_name=_("Discount percentage"))
    valid_from = models.DateTimeField(verbose_name=_("Valid From"))
    valid_to = models.DateTimeField(verbose_name=_("Valid To"))
    is_active = models.BooleanField(default=True,verbose_name=_("Active"))
    is_used = models.BooleanField(default=False,verbose_name=_("Used"))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='promocodes',verbose_name=_("User"))
    
    
    class Meta:
        verbose_name = _("Promo Code")
        verbose_name_plural = _("Promo Codes")
        ordering = ['-created_at']
        
    @property
    def period_time(self):
        return f"{self.valid_from.strftime('%Y-%m-%d %H:%M:%S')} - {self.valid_to.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def __str__(self):
        return self.code
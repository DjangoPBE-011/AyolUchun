from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.base.models import media_upload_to,BaseModel
from apps.accounts.models import PromoCode

# Create your models here.

User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True,verbose_name=_("Category Name"))
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
    
    

class Course(BaseModel):
    title = models.CharField(max_length=200,verbose_name=_("Course Title"))
    description = models.TextField(max_length=1000,verbose_name=_("Course Description"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_courses',verbose_name=_("Author"))
    image = models.ImageField(upload_to=media_upload_to, blank=True, null=True,verbose_name=_("Course Image"))
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name=_("Course Price"))    
    is_active = models.BooleanField(default=True,verbose_name=_("Course Status"))
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE, related_name='courses',verbose_name=_("Promo Code"), blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses',verbose_name=_("Course Category"))
    
    
    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
    
    
    
class Module(BaseModel):
    name = models.CharField(max_length=200,verbose_name=_("Module Name"))
    order = models.PositiveIntegerField(verbose_name=_("Module Order"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules',verbose_name=_("Course"))
    description = models.TextField(max_length=1000,verbose_name=_("Module Description"))
    
    class Meta:
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
    
    
def validate_video_size(file):
    max_size_mb = 50  # Chegara (MB)
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(_(f"Video hajmi {max_size_mb} MB dan oshmasligi kerak!"))
    
class Video(BaseModel):
    title = models.CharField(max_length=200,verbose_name=_("Video Title"))
    video_file = models.FileField(upload_to=media_upload_to,verbose_name=_("Video File"), validators=[validate_video_size])
    period_time = models.DateTimeField(verbose_name=_("Video Duration"))
    order = models.PositiveIntegerField(verbose_name=_("Video Order"))
    status = models.BooleanField(default=True,verbose_name=_("Video Status"),help_text=_("If the video is locked, we can see the filed is False, and if the video is unlocked, we can see the field is True."))
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='videos',verbose_name=_("Course Module"))
    period_time = models.DurationField(verbose_name=_("Video Duration"))
    
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments',verbose_name=_("User"), null=True, blank=True)
    content = models.TextField(max_length=1000,verbose_name=_("Comment"),null=True, blank=True)
    review = models.PositiveIntegerField(verbose_name=_("Review"),validators=[MinValueValidator(1), MaxValueValidator(5)],null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments',verbose_name=_("Course"))
    
    
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-created_at']
        
        
    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class Sertificate(BaseModel):
    name = models.CharField(max_length=200,verbose_name=_("Certificate Name"),null=True, blank=True)
    description = models.TextField(max_length=1000,verbose_name=_("Certificate Description"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates',verbose_name=_("User"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates',verbose_name=_("Course"))
    certificate_file = models.FileField(upload_to=media_upload_to,verbose_name=_("Certificate File"))
    
    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
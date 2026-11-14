import os
from django.db import models
from django.utils import timezone


# Create your models here.

def media_upload_to(instance, filename):
    # Faqat fayl nomi - aks holda upload_to ikki marta qo'shiladi yoki path bo'ladi
    safe = os.path.basename(filename) or "upload.jpg"
    return timezone.now().strftime("uploads/%Y/%m/%d/") + safe
    
    
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
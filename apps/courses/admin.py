from django.contrib import admin
from apps.courses.models import Category, Course, Module, Video, Comment, Sertificate


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'price')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'order', 'created_at')
    list_filter = ('course',)
    search_fields = ('name', 'description')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order', 'period_time', 'status', 'created_at')
    list_filter = ('status', 'module__course', 'created_at')
    search_fields = ('title',)
    list_editable = ('status', 'order')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'review', 'created_at')
    list_filter = ('review', 'created_at')
    search_fields = ('content', 'user__username', 'course__title')


@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'course', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'user__username', 'course__title')
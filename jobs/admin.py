from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'posted_by', 'created_at']
    list_filter = ['created_at', 'location']
    search_fields = ['title', 'company_name', 'location']
    date_hierarchy = 'created_at'
    list_per_page = 20


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'applied_at']
    list_filter = ['applied_at', 'job__company_name']
    search_fields = ['applicant__username', 'job__title', 'job__company_name']
    date_hierarchy = 'applied_at'
    list_per_page = 20 
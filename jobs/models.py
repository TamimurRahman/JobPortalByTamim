from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title} at {self.company_name}"
    
    class Meta:
        ordering = ['-created_at']


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"
    
    class Meta:
        ordering = ['-applied_at']
        unique_together = ['job', 'applicant'] 
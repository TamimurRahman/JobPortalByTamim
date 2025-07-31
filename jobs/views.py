from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Job, Application
from .forms import UserRegistrationForm, JobForm, ApplicationForm


def home(request):
    """Home page with featured jobs"""
    featured_jobs = Job.objects.all()[:6]
    return render(request, 'jobs/home.html', {'featured_jobs': featured_jobs})


def register(request):
    """User registration with role selection"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            # Store user type in session
            request.session['user_type'] = user_type
            messages.success(request, f'Account created successfully! Welcome {user.username}')
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'jobs/register.html', {'form': form})


@login_required
def dashboard(request):
    """Role-based dashboard"""
    user_type = request.session.get('user_type', 'applicant')
    
    if user_type == 'employer':
        # Employer dashboard
        posted_jobs = Job.objects.filter(posted_by=request.user)
        total_applications = Application.objects.filter(job__posted_by=request.user).count()
        context = {
            'posted_jobs': posted_jobs,
            'total_applications': total_applications,
            'user_type': 'employer'
        }
        return render(request, 'jobs/employer_dashboard.html', context)
    else:
        # Applicant dashboard
        my_applications = Application.objects.filter(applicant=request.user)
        context = {
            'my_applications': my_applications,
            'user_type': 'applicant'
        }
        return render(request, 'jobs/applicant_dashboard.html', context)


@login_required
def job_list(request):
    """Job listing with search functionality"""
    jobs = Job.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company_name__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'jobs/job_list.html', context)


@login_required
def job_detail(request, job_id):
    """Job detail view with application form"""
    job = get_object_or_404(Job, id=job_id)
    has_applied = False
    
    if request.user != job.posted_by:
        has_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    
    if request.method == 'POST' and not has_applied and request.user != job.posted_by:
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_detail', job_id=job.id)
    else:
        form = ApplicationForm()
    
    context = {
        'job': job,
        'form': form,
        'has_applied': has_applied,
    }
    return render(request, 'jobs/job_detail.html', context)


@login_required
def post_job(request):
    """Post a new job (employer only)"""
    user_type = request.session.get('user_type', 'applicant')
    if user_type != 'employer':
        messages.error(request, 'Only employers can post jobs.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('dashboard')
    else:
        form = JobForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})


@login_required
def my_jobs(request):
    """View jobs posted by the employer"""
    user_type = request.session.get('user_type', 'applicant')
    if user_type != 'employer':
        messages.error(request, 'Only employers can view their posted jobs.')
        return redirect('dashboard')
    
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})


@login_required
def job_applications(request, job_id):
    """View applications for a specific job (employer only)"""
    job = get_object_or_404(Job, id=job_id)
    
    if job.posted_by != request.user:
        messages.error(request, 'You can only view applications for your own jobs.')
        return redirect('dashboard')
    
    applications = Application.objects.filter(job=job)
    return render(request, 'jobs/job_applications.html', {
        'job': job,
        'applications': applications
    })


@login_required
def my_applications(request):
    """View user's submitted applications"""
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'jobs/my_applications.html', {'applications': applications}) 
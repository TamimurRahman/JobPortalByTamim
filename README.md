# Job Portal Application

A modern, attractive job portal built with Django that allows employers to post jobs and applicants to search and apply for positions.

## 🚀 Features

### User Roles
- **Employer**: Post jobs, view applications, manage job listings
- **Applicant**: Search jobs, apply with resume and cover letter, track applications

### Authentication & User Management
- User registration with role selection (Employer/Applicant)
- Login/logout functionality
- Role-based dashboard and navigation

### Job Management
- **For Employers:**
  - Post new job openings
  - View all posted jobs
  - See applications for each job
  - Download applicant resumes
  - Review cover letters

- **For Applicants:**
  - Browse all available jobs
  - Search jobs by title, company, or location
  - Apply to jobs with resume upload and cover letter
  - Track submitted applications

### Search Functionality
- Advanced job search by:
  - Job title
  - Company name
  - Location
- Real-time search results with pagination

### Modern UI/UX
- Responsive Bootstrap 5 design
- Gradient backgrounds and modern styling
- Interactive job cards with hover effects
- Professional dashboard layouts
- Mobile-friendly interface

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, Font Awesome
- **Forms**: Django Crispy Forms
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **File Upload**: Django's built-in file handling

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Pillow (for image/file handling)
- django-crispy-forms
- crispy-bootstrap5

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd JobPortalByTamim
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
JobPortalByTamim/
├── jobportal/                 # Main Django project
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── jobs/                     # Jobs app
│   ├── models.py            # Job and Application models
│   ├── views.py             # All view functions
│   ├── forms.py             # Form classes
│   ├── admin.py             # Admin panel configuration
│   └── urls.py              # App URL patterns
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   └── jobs/                # Job-related templates
├── media/                    # Uploaded files (resumes)
├── static/                   # Static files
├── requirements.txt          # Python dependencies
└── manage.py                # Django management script
```

## 🎯 Key Features Implementation

### Models
- **Job Model**: title, company_name, location, description, posted_by, created_at
- **Application Model**: job, applicant, resume, cover_letter, applied_at

### Views
- Home page with featured jobs
- User registration with role selection
- Role-based dashboards
- Job listing with search and pagination
- Job detail with application form
- Job posting for employers
- Application management

### Admin Panel
- Customized Job and Application admin interfaces
- Search and filter capabilities
- Relevant field displays

## 🎨 UI/UX Features

- **Modern Design**: Gradient backgrounds, card-based layouts
- **Responsive**: Works on desktop, tablet, and mobile
- **Interactive**: Hover effects, smooth transitions
- **Professional**: Clean typography and spacing
- **Accessible**: Proper contrast and navigation

## 🔍 Search Functionality

The job search feature allows users to search by:
- Job title (partial matches)
- Company name (partial matches)
- Location (partial matches)

Search results are paginated and display relevant information for each job.

## 📱 User Experience

### For Employers
1. Register as an employer
2. Post job openings with detailed descriptions
3. View and manage applications
4. Download applicant resumes
5. Track application statistics

### For Applicants
1. Register as an applicant
2. Browse available jobs
3. Search for specific positions
4. Apply with resume and cover letter
5. Track application status

## 🛡️ Security Features

- CSRF protection
- File upload validation
- User authentication
- Role-based access control
- Secure form handling

## 🚀 Deployment

The application is ready for deployment to platforms like:
- Heroku
- DigitalOcean
- AWS
- PythonAnywhere

## 📝 License

This project is created for educational purposes and can be used as a foundation for a job portal application.

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## 📞 Support

For any questions or support, please create an issue in the repository. #   J o b P o r t a l B y T a m i m  
 
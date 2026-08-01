"""
URL configuration for Student_CRUD_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Student_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_student, name='get_student'),
    path('create_type1/', views.create_student_type1, name='create_student_type1'),
    path('create_type2/', views.create_student_type2, name='create_student_type2'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update_type1/<int:student_id>/', views.update_student_type1, name='update_student_type1'),
    path('update_type2/<int:student_id>/', views.update_student_type2, name='update_student_type2'),

    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name='logout'),

]

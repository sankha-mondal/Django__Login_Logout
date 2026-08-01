## Create Superuser OR admin with passwd:
-----------------------------------------
    python manage.py createsuperuser
Username (leave blank to use 'sankmond'): admin
Email address: <stay blank>

Password: ****** 

Password (again): ******

Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

    http://localhost:8000/admin/

## Required changes to implement Login-Logout:
----------------------------------------------
setting.py

    LOGIN_REDIRECT_URL = '/'  # Redirect to home page after login
    LOGOUT_REDIRECT_URL = '/'  # Redirect to home page after logout

url.py

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name='logout'),

login.html

logout.html

    

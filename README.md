# 🌐 Create Superuser OR admin with passwd:
-----------------------------------------
    python manage.py createsuperuser
Username (leave blank to use 'sankmond'): admin
Email address: <stay blank>

Password: ****** 

Password (again): ******

Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

    http://localhost:8000/admin/

# 🌐 Required changes to implement Login-Logout:
----------------------------------------------
setting.py

    ## Login and Logout Redirect URLs
	LOGIN_REDIRECT_URL = '/'  # Redirect to home page after login
	LOGOUT_REDIRECT_URL = '/accounts/login/'  # Redirect to login page after logout

url.py

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name='logout'),

login.html

	<form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>


# 🌐 Operations:
--------------
### Login Page:
<img width="1871" height="959" alt="image" src="https://github.com/user-attachments/assets/3bbdab7f-b74d-4f46-adf6-ea37e7579103" />

### After Login:
<img width="1868" height="929" alt="image" src="https://github.com/user-attachments/assets/bb779af1-1c86-4629-b2de-b209e105087a" />

### User Add:
<img width="1871" height="891" alt="image" src="https://github.com/user-attachments/assets/f30a0af6-0c04-4f5d-9298-d0f5f0024413" />

### User Permissions:
<img width="1869" height="557" alt="image" src="https://github.com/user-attachments/assets/091d9fd2-f440-4eb8-9f81-64b11ee07a8a" />

### Group Permissions:
<img width="1855" height="851" alt="image" src="https://github.com/user-attachments/assets/00abc424-a911-46b2-94bb-01a5718caddc" />


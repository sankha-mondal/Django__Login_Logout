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


## Operations:
--------------
<img width="1871" height="959" alt="image" src="https://github.com/user-attachments/assets/3bbdab7f-b74d-4f46-adf6-ea37e7579103" />

<img width="1868" height="929" alt="image" src="https://github.com/user-attachments/assets/bb779af1-1c86-4629-b2de-b209e105087a" />




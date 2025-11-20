1. Create app:
   python manage.py startapp home

2. Add app to INSTALLED_APPS in settings.py

3. Create home/urls.py and add routes:
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.api_home),
   ]

4. Create view in home/views.py

5. Connect app URLs in project urls.py:
   path('', include('home.urls'))

Done. Now app routes work.
--------------------------------------------------------------------------------------------------

Serialization means converting Django model data into JSON so it can be sent over the internet (API response).
Define DB structure
create a serializer
create views with api_decorator for different type of request
and add routes
(also created a super User) 

---------------------------------------------------------------------------------------

to create new models u first create it in models.py and then register it in admin.py
instead of writing api_view for every method u can use APIView in class it gives you built in method to write code for every path

---------------------------------------------------------------------------------------
->for session authentication u first add 'rest_framework.authtoken'- in settings.py in Installed apps
->from rest_framework.authtoken import views
path('api-token-auth/', views.obtain_auth_token), - add these in core its mpore like for login
->for registration 
add serializer u can find model in import as User and then make view for registration for hashing there is serializer & methode set__password 
-> for authenticating routes u add these in settings.py 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}- and add methods in class of routes there are imports to create token and autrhentication in routes check that in home/views
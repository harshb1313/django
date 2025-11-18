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
----------------------------------------------------------------------------------

Serialization means converting Django model data into JSON so it can be sent over the internet (API response).
Define DB structure
create a serializer
create views with api_decorator for different type of request
and add routes
(also created a super User) 
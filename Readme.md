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
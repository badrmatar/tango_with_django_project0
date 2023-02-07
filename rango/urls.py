from django.urls import path
from rango import views
app_name = 'rango'
<<<<<<< HEAD
=======

>>>>>>> c2973e665a09b9ed026ccc6d656e7a1a25687726
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

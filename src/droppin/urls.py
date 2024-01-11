from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('booking/', views.booking, name="booking"),
    path('actualities/', views.actualities, name="actualities"),
    path('services/', views.services, name="services"),
    path('connect/', views.connect, name="connect"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('comment/', views.comment, name="comment"),
    path('<int:id>/', views.comment, name="comment"),
    path('contact/', views.contact, name="contact"),
]

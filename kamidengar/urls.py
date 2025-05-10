from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('homepage/', views.homepage, name='homepage'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),  # adjust names here
    path('createaccpage/', views.createaccpage, name='createaccpage'),
    path('profile/', views.profile, name='profile'),
    path('hazardselection/', views.hazardselection, name='hazardselection'),
    path('pothole/', views.pothole, name='pothole'),
    path('brokentrafficlight/', views.brokentrafficlight, name='brokentrafficlight'),
    path('fadedroadmark/', views.fadedroadmarking, name='fadedroadmarking'),
    path('illegaldumping/', views.illegaldumping, name='illegaldumping'),
    path('blockdrain/', views.blockdrain, name='blockdrain'),
    path('illegalparking/', views.illegalparking, name='illegalparking'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('termsandconditions/', views.termsandconditions, name='termsandconditions'),

]
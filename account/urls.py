from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('',views.index, name= "index"),
    path('profile/',views.profileView, name="profile"),
    path('login/',LoginView.as_view(), name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page ="index"), name="logout"),

]




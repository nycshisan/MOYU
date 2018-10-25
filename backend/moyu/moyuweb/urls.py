from django.urls import path

from . import views

app_name = "moyuweb"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('login_auth',views.login_auth, name="login_auth"),
    path('logout/',views.logout,name="logout"),
]
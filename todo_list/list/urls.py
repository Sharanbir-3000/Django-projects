from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home,name='home'),
    path("create/",views.create_task,name='create'),
    path("update/<int:pk>/",views.update_task,name='update'),
    path("deletion/<int:pk>/",views.deletion,name='delete'),
    path("view/<int:pk>/",views.view,name='view'),
    path("register/",views.register,name='register'),
    path("",views.loginpage,name='loginpage'),
    path("logout/",views.logout_page,name='logout'),
]
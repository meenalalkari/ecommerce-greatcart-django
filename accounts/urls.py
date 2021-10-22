from django.urls import path
from . import views

urlpatterns = [
    path('/register/',views.register,name='register'),
    path('/login/',views.login,name='login'),
    path('/logout/',views.logout,name='logout'),
    path('/activate/<uidb64>/<token>',views.activate,name='activate'),
    path('/forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('/resetpassword_validation/<uidb64>/<token>',views.resetpassword_validation,name='resetpassword_validation'),
    ]

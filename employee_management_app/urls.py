from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', start),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm)),
    path('change-password/', change_password),
    path('logout/', logout_view),
    path('home/',home),
    path('add-emp/',add_emp),
    path('emp-list/', emp_list),
    path('emp-detail/<int:id>', emp_detail),
    path('emp-update/<int:id>', emp_update),
    path('do-emp-update/<int:id>', do_emp_update)
]

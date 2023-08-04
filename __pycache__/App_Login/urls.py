from django.urls import path
from App_Login import views
from django.contrib.auth import views as auth_views

app_name = 'App_Login'

urlpatterns=[
    path('register/',views.register_attempt,name='register_attempt'),
    path('login/',views.login_attempt,name='login_attempt'),
    path('logout/',views.logout_user,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('subscriber_payment/',views.subscriber_payment,name='subscriber_payment'),
    path('token/',views.token_send,name='token_send'),
    path('success/',views.success,name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error/' , views.error_page , name="error_page")
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)



]

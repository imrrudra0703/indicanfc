from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Index.urls')),
    path('contactus/', include('contact.urls')),
    path('account/', include('App_Login.urls')),
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
    name="reset_password"),

   path('reset_password_sent/',
       auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
       name="password_reset_done"),

   path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
    name="password_reset_confirm"),

   path('reset_password_complete/',
       auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
       name="password_reset_complete"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

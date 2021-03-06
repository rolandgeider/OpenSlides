from django.conf.urls import url

from . import views

urlpatterns = [
    # Auth
    url(r'^login/$',
        views.UserLoginView.as_view(),
        name='user_login'),

    url(r'^logout/$',
        views.UserLogoutView.as_view(),
        name='user_logout'),

    url(r'^whoami/$',
        views.WhoAmIView.as_view(),
        name='user_whoami'),

    url(r'^setpassword/$',
        views.SetPasswordView.as_view(),
        name='user_setpassword'),

    # PDF
    url(r'^print/$',
        views.UsersListPDF.as_view(),
        name='user_listpdf'),

    url(r'^passwords/print/$',
        views.UsersPasswordsPDF.as_view(),
        name='user_passwordspdf'),
]

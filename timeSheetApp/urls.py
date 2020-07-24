from django.contrib import admin
from django.urls import path,include,re_path
from timeSheetApp import views
from django.views.i18n import JavaScriptCatalog
from django.conf.urls import url
from django.views.generic import RedirectView
import re

urlpatterns = [
    path('',views.index, name='home'),
    path('contact/',views.contact, name='contactUs'),
    path('memberDashboard/',views.memberDash,name="empDashboard"),
    path('memberDashboard/summary',views.summary,name='summary'),
    path('loginEmp/',views.loginEmp),
    path('loginAdmin/',views.loginAdmin),
    re_path(r'^logout/$',views.logoutUser,name='logout'),
    path('memberDashboard/user',views.users,name="empUser"),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

admin.site.site_header = 'TimeSheet Admin Panel'
admin.site.site_title = 'TimeSheet Admin Panel'
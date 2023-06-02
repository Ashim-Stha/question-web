from django.contrib import admin
from django.urls import path 
from home import views
admin.site.site_header = "ADMIN PANNEL"
admin.site.site_title = "QUESTIONPAPER ADMIN PANNEL"
admin.site.index_title = "Welcome to admin  Portal"
urlpatterns = [
  path("",views.index,name='home '),
  path("search/",views.search,name='search_view')
]

from django.conf.urls import url
from fourapp import views

#Template Tagging

app_name='fourapp'

urlpatterns=[
    url('other/',views.other,name='other'),
    url('relative/',views.relative,name='relative'),
    url('inher/',views.inher,name='inher'),
]
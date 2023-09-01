from django.urls import path
from sa.views import *
app_name='sa'
urlpatterns=[
    path("saca/",saca,name='saca'),
    path("south/",south,name='south'),
]
from django.urls import path
from app1.views  import *
app_name='fayyu1'


urlpatterns=[
    path('python/',python,name='python'),
]
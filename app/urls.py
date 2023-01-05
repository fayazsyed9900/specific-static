from django.urls  import path
from app.views import *
app_name='fayyu'

urlpatterns=[
    path('django/',django,name='django'),
]
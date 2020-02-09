from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
     url(r'^submit/expense/$', views.submit_expense, name='subimt_expense'),
#    path('expense/', views.submit_expense, name='subimt_expense')
]

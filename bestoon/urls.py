from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
     url(r'^submit/expense/$', views.submit_expense, name='subimt_expense'),
     url(r'^submit/income/$', views.submit_income, name='submit_income'),
]

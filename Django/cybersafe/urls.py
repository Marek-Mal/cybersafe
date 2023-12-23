from django.urls import path
from cybersafe.views import get_question, SendEmailView, get_question_filter
from rest_framework import routers


urlpatterns = [
    path('get/', get_question.as_view(), name='get_email_content'),
    path('filter/', get_question_filter.as_view(), name='get_email_content'),
    path('send_email/', SendEmailView, name='send_email'),
]

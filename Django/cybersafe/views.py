from django.shortcuts import render
from django.contrib.auth.models import User
from cybersafe.serializers import Questions_serializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from cybersafe.models import Questions
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q
from rest_framework.response import Response


class get_question(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = Questions_serializer
    permission_classes = []
    http_method_names = ['get']

class get_question_filter(generics.ListAPIView):
    serializer_class = Questions_serializer
    permission_classes = []
    http_method_names = ['get']

    def get_queryset(self):
        # Get the search query parameter from the request
        query = self.request.query_params.get('query', '')

        # Filter questions based on the search query
        queryset = Questions.objects.filter(
            Q(question__icontains=query)  # Case-insensitive text search on the 'question' field
        )

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

@csrf_exempt
def SendEmailView(req):
    if req.method == "POST":

        try:
            json_data = json.loads(req.body.decode('utf-8'))
            
            whoami = json_data.get('whoami', '')
            message = json_data.get('que_short', '')  # Adjust the key names
            subject = json_data.get('que_long', '')  # Adjust the key names

            send_mail(
                message,
                subject + "\n\n" + whoami,
                'settings.EMAIL_HOST_USER',
                ['cyberbezpieczni.contact@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Email sent successfully'})
        except json.JSONDecodeError as e:
            print('Error decoding JSON:', e)
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
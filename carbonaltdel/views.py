from rest_framework.views import APIView

from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request, format=None):
        return Response('Hello, this is the Django REST API for www.carbonaltdel.com')

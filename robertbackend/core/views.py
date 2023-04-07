from core.models import Test
from core.serializers import TestSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MyView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    authentication_classes = []
    permission_classes = []
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    http_method_names = ['get','post','patch']

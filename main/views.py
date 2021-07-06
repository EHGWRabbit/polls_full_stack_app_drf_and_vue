from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .serializers import CrySerializer, ProblemSerializer
from .models import Problem
from django.db import IntegrityError


def ip_person(request):
    x_for = request.META.get('HTTP_X_FOR')
    if x_for:
        address = x_for.split(',')[0]
    else:
        address = request.META.get('REMOTE')
    return address


class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all().order_by('-votes')
    serializer_class = ProblemSerializer
    permission_classes = [IsAdminUser, ]


class ListProblemView(APIView):
    def post(self, request):
        serializer = CrySerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            created_instance = serializer.create(validated_data=request.data)
            created_instance.address = ip_person(request)

            try:
                created_instance.save()
            except IntegrityError:
                return Response(
                    {'message': 'Уже отправлен ваш выбор'}, 
                    status = status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {'message': 'Ваш выбор успешно отправлен'},
                status = status.HTTP_200_OK
            )



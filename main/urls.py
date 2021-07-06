from django.urls import include, path
from rest_framework import routers
from . import views as main_views


router = routers.DefaultRouter()
router.register(r'problem', main_views.ProblemViewSet)

app_name = 'api'

urlpatterns = [
    path('cry/', main_views.ListProblemView.as_view(), name='cry'),
]
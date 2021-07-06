from rest_framework import serializers
from main.models import Problem, Cry
from django.shortcuts import get_object_or_404
from django.db import IntegrityError


class ProblemSerializer(serializers.ModelSerializer):
    cryes = serializers.ReadOnlyField()

    class Meta:
        model = Problem 
        fields = '__all__'


class CrySerializer(serializers.ModelSerializer):
    problem_title = serializers.CharField()
    def born(self, validated_data):
        problem = get_object_or_404(Problem, name=validated_data['problem_title'])
        cry = Cry()
        cry.problem = problem 
        try:
            cry.save(commit=False)
        except IntegrityError:
            return cry 
        return cry 

    class Meta:
        model = Cry
        exclude = ('id', 'ip_address', 'problem')
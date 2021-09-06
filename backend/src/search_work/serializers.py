from django.db.models import fields
from rest_framework import serializers

from . import models


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resume
        fields = ['pk', '_specialty', '_count_work']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'pk',
            '_first_name',
            '_second_name',
            '_phone_number',
            '_email',
            '_resume'
            ]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            'pk',
            '_city_name',
            '_person'
        ]

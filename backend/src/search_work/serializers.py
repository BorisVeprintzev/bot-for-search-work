from rest_framework import serializers

from . import models


class ResumeSerializer(serializers.ModelSerializer):
    _speciality = models.CharField(max_length=50)
    _count_works = models.IntegerField()

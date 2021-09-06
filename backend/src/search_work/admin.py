from django.contrib import admin
from . import models


class ResumeAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        '_specialty',
        '_count_works'
        ]
    list_editable = [
        '_specialty',
        '_count_works'
    ]


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        '_first_name',
        '_second_name',
        '_phone_number',
        '_email',
    ]
    list_editable = [
        '_first_name',
        '_second_name',
        '_phone_number',
        '_email',
    ]


class CityAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        '_city_name'
    ]
    list_editable = [
        '_city_name'
    ]


admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.City, CityAdmin)

from django.db import models

# TODO
# Create 3 tables with one-to-one response
# Person: first name, second name, phone number, email
# Resume: speciality, work experience (text), count works before
# City: city name


# In future, need to download list of speciality (for example from api.hh.ru)
class Resume(models.Model):
    _speciality = models.CharField(max_length=50)
    _count_works = models.IntegerField()

    def __str__(self):
        return f'''
            Speciality: {self.speciality},
            count works before: {self.count_works}
        '''


class Person(models.Model):
    _first_name = models.CharField(max_length=16)
    _second_name = models.CharField(max_length=32)
    _phone_number = models.CharField(max_length=11)
    _email = models.EmailField()
    _resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'''
            ID:\t\t\t{self.pk}
            First name:\t{self.first_name},\n
            Second name:\t{self.second_name},\n
            Phone number:\t{self.phone_number},\n
            Email:\t\t{self.email}
        '''


# In future, need to download list of cites (for example from api.hh.ru)
class City(models.Model):
    _city_name = models.CharField(max_length=20)
    _person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )

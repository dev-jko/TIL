from django.db import models
from faker import Faker


class Client(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

    @classmethod
    def dummy(cls, n):
        faker = Faker()
        for i in range(n):
            cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client, related_name='hotels')

    @classmethod
    def dummy(cls, n):
        faker = Faker()
        for i in range(n):
            cls.objects.create(name=faker.company())


class Student(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    title = models.CharField(max_length=100)


class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

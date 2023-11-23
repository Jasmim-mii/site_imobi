from django.contrib.auth.models import User
from django.db import models


class Visualization(models.Model):
    date_Visualization = models.CharField(max_length=20)

    def __str__(self):
        return self.date_Visualization


class Image(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url


class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class Time(models.Model):
    hours = models.TimeField()

    def __str__(self):
        return str(self.hours)


class Real_estate(models.Model):
    choices = (('V', 'Venda'),
               ('A', 'Alguel'))
    choices_imovel = (('A', 'Apartamento'),
                      ('C', 'Casa'))

    image = models.ManyToManyField(Image)
    price = models.FloatField()
    room = models.IntegerField()
    dimension = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=50)
    location = models.CharField(max_length=1, choices=choices)
    type_imovel = models.CharField(max_length=1, choices=choices_imovel)
    number = models.IntegerField()
    describe = models.TextField()
    visualization_day = models.ManyToManyField(Visualization)
    time = models.ManyToManyField(Time)

    def __str__(self) -> str:
        return self.street


class Visit(models.Model):
    choice = (('S', 'Segunda'),
              ('T', 'Terça'),
              ('Q', 'Quarta'),
              ('Q', 'Quinta'),
              ('S', 'Sexta'),
              ('S', 'Sabado'),
              ('D', 'Domingo'))

    choice_status = (('A', 'Agendado'),
                     ('F', 'Finalizado'),
                     ('C', 'Cancelado'))

    imovel = models.ForeignKey(Real_estate, on_delete=models.DO_NOTHING)
    user_visualization = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time_select = models.CharField(max_length=20)
    time_visualization = models.TimeField()
    status = models.CharField(max_length=1, choices=choice_status, default="A")

    def __str__(self) -> str:
        return self.user_visualization.username

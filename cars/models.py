from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    # a function abaixo diz ao django que ira ser feita uma ligacao na tabela de dados
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='car_brand'
    )
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    # magic method do Python para fazer retornar um nome mais legível na página do /admin do Django (No projeto)
    # Nesse caso, vai retornar o campo model como nome do objeto.
    def __str__(self):
        return self.model

from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Winery(models.Model):

    class Meta:
        verbose_name_plural = 'Wineries'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Grape(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Wine_type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Wine(models.Model):
    COUNTRY = (
        ('England', 'England'),
        ('Wales', 'Wales'),
    )
    sku = models.CharField(max_length=254, null=True, blank=True) 
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    wine_type = models.ForeignKey('Wine_type', null=True, on_delete=models.SET_NULL)
    country = models.CharField(max_length=254, null=True, blank=True, choices=COUNTRY)
    region = models.ForeignKey('Region', null=True, on_delete=models.SET_NULL)
    winery = models.ForeignKey('Winery', null=True, on_delete=models.SET_NULL)
    grape = models.ManyToManyField('Grape')
    tasting_notes = models.TextField(null=True, blank=True)
    pairing_suggestion = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    abv = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name




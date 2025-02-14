from django.db import models

class Product(models.Model):
    Top_Sale = 'Top Sale Watches'
    Feature = 'Feature Watches'
    New_Arrivals = 'New Arrivals'

    TAG = (
        (Top_Sale, 'Top Sale Watches'),
        (Feature, 'Feature Watches'),
        (New_Arrivals, 'New Arrivals'),
    )

    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.FloatField()
    tag = models.CharField(choices=TAG, max_length=150)


    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name

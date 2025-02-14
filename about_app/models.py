from django.db import models

class About(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURLs(self):
        urls = []
        if self.image1 and hasattr(self.image1, 'url'):
            urls.append(self.image1.url)
        if self.image2 and hasattr(self.image2, 'url'):
            urls.append(self.image2.url)
        return urls

    def __str__(self):
        return self.title
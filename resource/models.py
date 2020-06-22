from django.db import models

# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=200)

    def __str__(self):
        return self.resource_name


class ResourceLinks(models.Model):
    rlink_id = models.ForeignKey(Resource,on_delete=models.CASCADE)
    rlink = models.URLField(max_length = 1000)
    rtype = models.CharField(max_length=50)
    rdesp = models.CharField(max_length=300)
    rfiles = models.FileField(upload_to='uploads/',blank=True)

    def __str__(self):
        return self.rtype
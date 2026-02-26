from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage,RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage
# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    image = models.ImageField(upload_to='images/',storage=MediaCloudinaryStorage)
    video = models.FileField(upload_to='videos/',storage=VideoMediaCloudinaryStorage)
    pdf = models.FileField(upload_to='files/',storage=RawMediaCloudinaryStorage)
    
    def __str__(self):
        return self.name
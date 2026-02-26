from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    image = models.ImageField(upload_to="uploads/images/")
    video = models.FileField(upload_to="uploads/videos/")
    pdf = models.FileField(upload_to="uploads/pdfs/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

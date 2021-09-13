from django.db import models

PROGRESS_CHOICES =(
    ("Todo", "Todo"),
    ("Pending", "Pending"),
    ("Done", "Done"),
)

# Create your models here.
class card (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    choseprogress= models.CharField(max_length=100, choices=PROGRESS_CHOICES)
    comment=models.TextField()

    def __str__(self):
        return (self.name)
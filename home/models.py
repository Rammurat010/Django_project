from django.db import models

# Create your models here.

#makemigrations means create changes and store in a file
#migrate- apply the pending changes credited by makemigrations 
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    decs=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
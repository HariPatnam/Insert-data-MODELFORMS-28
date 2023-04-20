from django.db import models

# Create your models here.
 
class TOPIC(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name
    
class WEBPAGE(models.Model):
    topic_name=models.ForeignKey(TOPIC,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class ACCESSRECORDS(models.Model):
    name=models.ForeignKey(WEBPAGE,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.author
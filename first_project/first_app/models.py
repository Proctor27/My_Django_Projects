from django.db import models

class Users(models.Model):
    usernames = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.usernames
    
class Details(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    ipv4 = models.GenericIPAddressField(unique=True) 
    catchphrase = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.users.usernames
 
class Descriptions(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    # Changed these to TextField for better handling of long strings
    sentences = models.TextField() 
    paragraphs = models.TextField()
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.users.usernames} - {self.date}"
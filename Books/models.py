from django.db import models

class Book(models.Model):
    title = models.CharField('Title', max_length=50)
    pdf = models.FileField(upload_to = 'Books/pdfs/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
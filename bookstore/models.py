from django.db import models

# Create your models here.
class Book(models.Model):
    # slug = models.SlugField()
    name = models.CharField("Book Name", max_length=255, unique=True)
    description = models.TextField("Book Description")
    rate = models.PositiveIntegerField(default=0) 
    prod_date = models.DateField(null=True)
    
    def __str__(self):
        return f"Title {self.name}"
    # class Meta:
    #     ordering = ['created_at']
    #     verbose_name = "Movie Model"
    #     verbose_name_plural = "Movies"
    #     db_name = "movies"
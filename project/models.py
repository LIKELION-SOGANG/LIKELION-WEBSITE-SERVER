from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    generation = models.IntegerField()
    year = models.IntegerField()
    team_name = models.CharField(max_length=100)
    member_list = models.CharField(max_length=255)
    project_image = models.FileField()
    content = models.TextField()
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
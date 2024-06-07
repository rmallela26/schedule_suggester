from django.db import models

class Schedule(models.Model):
    pennkey = models.CharField(max_length=100) #allow mulitple same pennkeys, signifying same person over multiple terms 
    gpa = models.FloatField()
    semester = models.IntegerField(default=1) #which semester are they in?
    answers = models.JSONField()
    courses = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.pennkey
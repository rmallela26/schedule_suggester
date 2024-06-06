from django.db import models

class Schedule(models.Model):
    pennkey = models.CharField(max_length=100, unique=True)
    gpa = models.FloatField()
    semester = models.IntegerField(default=1) #which semester are they in?
    answers = models.JSONField()
    courses = models.TextField()
    review = models.TextField()
    # keep something to measure degree of change in each term
    # (change compared to last term's answers)
    # if someone changed their major, large degree of change
    # when pulling schedules sort by degree of change 
    # so even if someone now wants software, but didn't want 
    # software before, don't show their schedule

    def __str__(self):
        return self.pennkey
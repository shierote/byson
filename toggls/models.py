from django.db import models

class Project(models.Model):
    pid = models.IntegerField()
    project = models.CharField(max_length=250)
    project_hex_color = models.CharField(max_length=50)

class Task(models.Model):
    tid = models.IntegerField()
    description = models.CharField(max_length=250)
    start = models.DateTimeField('date started')
    end = models.DateTimeField('date ended')
    dur = models.IntegerField(default=0)
    expected_dur = models.IntegerField(default=0)
    gap_ratio = models.IntegerField(default=0)
    pid = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


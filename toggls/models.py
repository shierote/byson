from django.db import models

class Project(models.Model):
    pid = models.IntegerField()
    project = models.CharField(max_length=250)
    project_hex_color = models.CharField(max_length=50)

    def __str__(self):
        return self.project

class Task(models.Model):
    description = models.CharField(
            max_length=250,
            blank=True,
            null=True
            )
    start = models.DateTimeField(
            'date started',
            )
    end = models.DateTimeField(
            'date ended',
            )
    dur = models.IntegerField(default=0)
    expected_dur = models.IntegerField(
            blank=True,
            null=True
            )
    pid = models.IntegerField(
            blank=True,
            null=True
            )
    project = models.ForeignKey(
            Project,
            on_delete=models.SET_NULL,
            blank=True,
            null=True
            )

    def __str__(self):
        return self.description

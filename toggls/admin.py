from django.contrib import admin
from .models import Project, Task

class TaskAdmin(admin.ModelAdmin):
  fieldsets = [
          (None,                   {'fields': ['description']}),
          ('Date information',     {'fields': ['start', 'end']}),
          ('Duration information', {'fields': ['dur', 'expected_dur']}),
          ('Project information',  {'fields': ['pid', 'project']}),
  ]
  list_display = ('description', 'start', 'end', 'dur', 'expected_dur','project')
  list_filter = ['start', 'project']
  search_fields = ['description']
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)

from django.contrib import admin
from .models import School, Degree, Module, StudentModule, PinnedModule

admin.site.register(School)
admin.site.register(Degree)
admin.site.register(Module)
admin.site.register(StudentModule)
admin.site.register(PinnedModule)

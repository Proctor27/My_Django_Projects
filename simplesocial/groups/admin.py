from django.contrib import admin
from . import models  
# Register your models here.
#inline class to make a parent model have access to a parent model

class GroupMemberInline(admin.TabularInline):
        model = models.GroupMember



admin.site.register(models.Group)

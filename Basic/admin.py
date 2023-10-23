from django.contrib import admin

# Register your models here.
from .models import Skill, Project, Experience,SocialLink,Education,Achievement,Certificate

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(SocialLink)
admin.site.register(Education)
admin.site.register(Achievement)
admin.site.register(Certificate)
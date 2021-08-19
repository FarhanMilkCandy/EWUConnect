from django.contrib import admin
from .models import *


admin.site.register(UserModel)
admin.site.register(ProfileModel)
admin.site.register(EducationModel)
admin.site.register(WorkExperienceModel)
admin.site.register(AwardModel)

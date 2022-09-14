from django.contrib import admin

# Register your models here.
from .models import Doctor
from .models import Patient
from .models import Allergies
from .models import illnesses
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Allergies)
admin.site.register(illnesses)
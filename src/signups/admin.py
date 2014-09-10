from django.contrib import admin

# Register your models here.
from signups.models import Signup

"""class SignupAdmin(admin.ModelAdmin):
	class Meta:
		model = Signup"""
admin.site.register(Signup)
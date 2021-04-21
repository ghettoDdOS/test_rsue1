from django.contrib import admin
from test_auth.models import Person


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'corp', 'phone', 'mail')
    list_filter = ['corp']


admin.site.register(Person, PersonAdmin)

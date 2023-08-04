from django.contrib import admin
from .models import Details, Exhibition, Open_Mic, Newsletter, Comment
# Register your models here.

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'date']

admin.site.register(Exhibition)
admin.site.register(Open_Mic)
admin.site.register(Newsletter)
admin.site.register(Comment)
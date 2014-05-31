from django.contrib import admin
from models import *

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
	list_display = ('title','user','datetime','votes')
	list_filter=('user',)
	ordering = ('-id',)
	search_fields = ('title',)

admin.site.register(Message,MessageAdmin)
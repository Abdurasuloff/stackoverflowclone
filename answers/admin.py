from django.contrib import admin
from .models import Answer, Reply, Likes
# Register your models here.

admin.site.register(Answer)
admin.site.register(Reply)
admin.site.register(Likes)



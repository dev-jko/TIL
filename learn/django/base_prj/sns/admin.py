from django.contrib import admin

from .models import Posting, Comment


# Register your models here.

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Posting, PostingModelAdmin)


class CommendModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Comment, CommendModelAdmin)

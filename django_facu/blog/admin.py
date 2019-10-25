from django.contrib import admin
from .models import Post, PostDetail, Presentation, Presentation_ImageOnline

# Register your models here.
admin.site.register(Post)
admin.site.register(PostDetail)
admin.site.register(Presentation)
admin.site.register(Presentation_ImageOnline)

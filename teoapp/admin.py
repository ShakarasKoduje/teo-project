from django.contrib import admin

# Register your models here.
from teoapp.models import PostData, PostAuthor, PostContent


admin.site.register(PostData)
admin.site.register(PostAuthor)
admin.site.register(PostContent)
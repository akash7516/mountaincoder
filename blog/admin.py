from django.contrib import admin
from blog.models import Blog, Contact, Signup, Photo
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display=['sno','title']
    class Media:
        css={'all':("css/main.css",)}
        js=("js/blog.js",)

admin.site.register(Blog,BlogAdmin)

    
admin.site.register(Photo)
admin.site.register(Contact)
admin.site.register(Signup)
from django.contrib import admin
from .models import Post


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'content_type', 'og_image',
                    'og_image_alt', 'description', 'author',
                    'robots', 'body', 'publish', 'status']
    
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author'] 
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 
    show_facets = admin.ShowFacets.ALWAYS

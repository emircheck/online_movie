from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.movies.models import Movie, MovieImage


class InlineMovieImage(admin.TabularInline):
    model = MovieImage
    extra = 1
    fields = ['image', ]


class MovieAdminDisplay(admin.ModelAdmin):
    inlines = [InlineMovieImage, ]
    list_display = ('title', 'genre', 'description', 'image')
    search_fields = ('title', )
    list_filter = ('genre', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ''


admin.site.register(Movie, MovieAdminDisplay)

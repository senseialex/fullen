from django.contrib import admin
from models import Categoria, Enlace, Agregador
from actions import export_as_csv

class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'enlace', 'categoria', 'imagen_rosada', 'es_popular')
    list_editable = ('titulo', 'enlace', 'categoria')
    list_display_links = ('es_popular',)
    list_filter = ('categoria', 'usuario')
    search_fields = ('categoria__titulo', 'usuario__email', 'titulo')
    actions = [export_as_csv]
    raw_id_fields = ('categoria', 'usuario')

    def imagen_rosada(self, obj):
        url = obj.dar_imagen_votos_rosada()
        tag = '<img src="%s"/>' % url
        return tag
    imagen_rosada.allow_tags = True
    imagen_rosada.admin_order_field = 'votos'

class EnlaceInline(admin.StackedInline):
    model = Enlace
    extra = 3

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [EnlaceInline]

class AgregadorAdmin(admin.ModelAdmin):
    filter_vertical = ('enlaces',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace, EnlaceAdmin)
admin.site.register(Agregador, AgregadorAdmin)

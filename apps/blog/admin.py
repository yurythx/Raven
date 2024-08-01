from django.contrib import admin
from .models import Post, Categoria, Tag, Comentario
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome_tag', 'slug',
    list_display_links = 'nome_tag',
    search_fields = 'id', 'nome_tag', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('nome_tag',),
    }


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome_categoria', 'slug',
    list_display_links = 'nome_categoria',
    search_fields = 'id', 'nome_categoria', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('nome_categoria',),
    }

class PostAdmin(SummernoteModelAdmin):

    list_display = ('id','titulo_post', 'autor_post', 'data_post', 
                    'categoria_post','publicado_post',)

    list_editable = ('publicado_post',)

    list_display_links = ('id', 'titulo_post',)

    summernote_fields = ('conteudo_post', )



@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome_comentario', 'email_comentario', 
                    'post_comentario', 'data_comentario',
                    'publicado_comentario', )

    list_editable = ('publicado_comentario', )

    list_display_links = ('id', 'nome_comentario', 'email_comentario', )      


admin.site.register(Post, PostAdmin)    
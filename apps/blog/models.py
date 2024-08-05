from django import forms
from django.db import models
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField




from django.contrib.auth.models import User
#
from django.utils import timezone
from utils.images import resize_image
from utils.rands import slugify_new


#class PostAttachment(AbstractAttachment):
#    def save(self, *args, **kwargs):
#        if not self.name:
#            self.name = self.file.name

 #       current_file_name = str(self.file.name)
 #       super_save = super().save(*args, **kwargs)
 #       file_changed = False

 #       if self.file:
 #           file_changed = current_file_name != self.file.name
#
 #       if file_changed:
  #          resize_image(self.file, 900, True, 70)

#        return super_save


class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    nome_categoria = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)     

    def __str__(self):
        return self.nome_categoria 
    

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    nome_tag = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs) 

    def __str__(self):
        return self.nome_tag    

class Post(models.Model):

    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=255)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Nome do Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data da Publicação')
    conteudo_post = models.TextField(verbose_name='Titulo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.titulo_post   
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.titulo_post, 4)
        return super().save(*args, **kwargs)
    


class Comentario(models.Model):

    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False) # lembrar na hora de refatorar de colocar o nome Publicado_comentario

    def __str__(self):
        return self.nome_comentario        
    


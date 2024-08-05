from audioop import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Post
from .forms import PostForm
from django.db.models import Q, Count, Case, When
from blog.forms import FormComentario
from blog.models import Comentario
from django.contrib import messages


class PostCreate(CreateView):

    model = Post
    form_class = PostForm
    #fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post']
    template_name = 'blog/novo_post.html'
    success_url ="/"
    success_message = "Post adicionado com sucesso"
    

 
class PostUpdateView(UpdateView):
    
    model = Post
    
    fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post']
    template_name = 'blog/editar_post.html'
    success_url ="/"

class PostDeleteView(DeleteView):  
    model = Post  
    template_name = 'blog/deletar_post.html'
    success_url ="/"


class PostIndex(ListView):

   model = Post #model usado para preencher 
   template_name = 'blog/blog_index.html'#direcionando para o template
   #paginate_by = 3 # quantos posts vao ficar na pagina
   context_object_name = 'posts'#objeto de busca

   #funcao para colocar os posts em ordem do ultimo adicionado(mais recente)
   def get_queryset(self):
       qs = super().get_queryset()# refazendo o query set com a variavel qs
       qs = qs.order_by('-id').filter(publicado_post=True)#ordenando os posts na variavel qs e faz a busca apenas nos postes publicados

       qs = qs.annotate(# parte da funçao que separa os comentarios publicados

           numero_comentarios=Count( #Count = contar
               Case( #Case = caso
                   When(comentario__publicado_comentario=True, then=1) #when = quando obs : lembrar na hora de refatorar de colocar o nome Publicado_comentario

               )
           )

       )

       return qs

class PostBusca(PostIndex):

    template_name = 'blog/posts_busca.html'#direcionando para o template

    def get_queryset(self):
        qs = super().get_queryset() #começa a fazer a busca

        termo = self.request.GET.get('termo') # usa o argumento termo referenciado no html no label da busca

        if not termo: # se a busca retornar vazia
            return qs # retorna qs vazio

        qs = qs.filter( # fazendo filtro no campo de busca

            # os campos abaixo fazem a busca pelos campo especificados no models

           Q(titulo_post__icontains=termo) |
           Q(autor_post__first_name__iexact=termo) |
           Q(conteudo_post__icontains=termo) |
           Q(excerto_post__icontains=termo) |
           Q(categoria_post__nome_categoria__iexact=termo) 

           # icontains faz a busca sem case sensitive e iexact tambem faz a busca sem case sensitive mas para chave estrangeira

        )

        return qs


class PostCategoria(PostIndex):

    template_name = 'blog/posts_categoria.html'#direcionando para o template

    def get_queryset(self): #começa a fazer a busca por categorias
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_categoria__iexact=categoria)    
        # o filtro acima busca a chave estrangeira categoria e em seguida com o __ busca o campo e en seguda __ o iexact faz a busca sem case sensitive


        return qs


class PostDetalhes(UpdateView):
    
    template_name = 'blog/post_detalhes.html'#direcionando para o template
    model = Post #model usado para preencher 

    form_class = FormComentario

    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        contexto = super().get_context_data(**kwargs)

        post = self.get_object()

        comentarios = Comentario.objects.filter(publicado_comentario=True,
                                                post_comentario=post.id )

        contexto ['comentarios'] = comentarios                                       


        return contexto
    
    def form_valid(self, form):

        post = self.get_object()

        comentario = Comentario(**form.cleaned_data)

        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()   

        messages.success(self.request, 'Comentário enviado com sucesso!!!') 

        return redirect('post_detalhes', pk=post.id)

       
        
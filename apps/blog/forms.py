from django import forms
from django.forms import ModelForm
from .models import Post
from .models import Comentario
from django_summernote.widgets import SummernoteWidget



class PostForm(forms.ModelForm):

    #content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        
        # fields = '__all__' esse metodo usa todos os campos no formulario
        # fields = ('nome', 'telefone')  esse é o metodo que esta sendo usado
        # exclude = ('celular', 'email')
        
        fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post']

        widgets = {
            'Titulo': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'Sumário': forms.Textarea(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            'Conteúdo': SummernoteWidget(),
            'Autor': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'Categoria': forms.Select(attrs={'placeholder':'Post', 'class': 'form-control form-control-lg'}),
            'imagem': forms.FileInput(attrs={'id':'validatedCustomFile'}),
        }



class FormComentario(ModelForm):

    def clean(self):

        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        

        print(data)

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
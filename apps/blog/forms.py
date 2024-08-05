from django import forms
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post
from .models import Comentario


class PostForm(forms.ModelForm):

    

    class Meta:
        model = Post
        
        # fields = '__all__' esse metodo usa todos os campos no formulario
        # fields = ('nome', 'telefone')  esse é o metodo que esta sendo usado
        # exclude = ('celular', 'email')
        
        fields = ['titulo_post', 'excerto_post', 'conteudo_post', 'autor_post', 'categoria_post', 'imagem_post']

        widgets = {
            'Titulo': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'Sumário': forms.Textarea(attrs={'placeholder':'Súmario', 'class': 'form-control form-control-lg'}),
            'Conteúdo': forms.CharField(label='Html:',widget=CKEditorUploadingWidget(attrs={'autocomplete': True})),
            #'Conteúdo': forms.CharField(widget=CKEditorUploadingWidget()),
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
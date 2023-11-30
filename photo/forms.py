from django.forms import ModelForm
from .models import PhotoPost
from django import forms


class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']
        
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # widgetのattrsにplaceholderを指定すると、テンプレート作成時に以下を生成する
        # <input type="text" placeholder="お名前を入力して下さい">
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力して下さい'
        # widgetのattrsにclassを指定すると、テンプレート作成時に以下を生成する
        # <input type="text" class="form-control">
        self.fields['name'].widget.attrs['class'] = 'form-control'
        # 2つまとめて生成するので、最終的な出力は以下の通り
        # <input type="text" placeholder="お名前を入力して下さい" class="form-control">
        
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'
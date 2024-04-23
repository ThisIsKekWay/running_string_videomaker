from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='Текст')
    text_color = forms.CharField(label='Цвет текста', widget=forms.TextInput(attrs={'type': 'color'}))
    background_color = forms.CharField(label='Цвет фона', widget=forms.TextInput(attrs={'type': 'color'}))

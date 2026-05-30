from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Links, Category


class LinksForm(forms.ModelForm):
    title = forms.CharField(
        label=_('Додайте опис до свого Link (необов\'язково)'),
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Опис'),
            'rows': '2',
        })
    )
    link = forms.CharField(
        label=_('Ваш короткий Link'),
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Link')
        })
    )
    origin_url = forms.CharField(
        label=_('Ваш URL - адрес'),
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('URL')
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label=_('Категорія (необов\'язково)'),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    privacy = forms.BooleanField(
        label=_('Чи є цей URL приватним?'),
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check',
        })
    )
    class Meta:
        model = Links
        fields = ('title', 'link', 'origin_url', 'category', 'privacy')
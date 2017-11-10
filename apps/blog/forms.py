# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/9 下午8:22'

from django import forms
from .models import Post


class PostWriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/10 下午12:47'

from django import forms

from .models import PostComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)

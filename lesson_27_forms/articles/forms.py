from django import forms

from articles.models import Article
from articles.constants import BAD_WORDS

from django.core.exceptions import ValidationError


class ContentArticleField(forms.Field):
    widget = forms.Textarea(attrs={'rows': 10})

    def to_python(self, value):
        if not value:
            return None

        return value

    def validate(self, value):
        for phrase in BAD_WORDS:
            if phrase in value:
                raise ValidationError('Незя так писать')
        return value


class ArticleCreateForm(forms.ModelForm):
    content = ContentArticleField()

    class Meta:
        model = Article
        fields = ('title', 'content', 'count_views', 'email')

        widgets = {
            'email': forms.TextInput()
        }


from django.forms import ModelForm
from .models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_body']

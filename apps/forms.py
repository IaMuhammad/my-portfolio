from django.forms import ModelForm

from apps.models import Portfolio, Message


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title', 'category')

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, FormView

from apps.forms import MessageForm
from apps.models import Portfolio, Message, Category, User, Skill, Education


# from apps.models import FeedBackView


# Create your views here.
class HomeView(FormView):
    form_class = MessageForm
    template_name = 'apps/index.html'
    success_url = reverse_lazy('home_view')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = User.objects.filter(username='muhammad').first()
        context['users'] = User.objects.filter(~Q(username='muhammad'))
        skills = Skill.objects.order_by('-percentage')
        context['skills1'] = skills[0::2]
        context['skills2'] = skills[1::2]
        context['educations'] = Education.objects.all()
        context['categories'] = Category.objects.all()
        context['portfolios'] = Portfolio.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class PortfolioDetailView(DetailView):
    model = Portfolio
    slug_url_kwarg = 'slug'
    template_name = 'apps/portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = kwargs['object']
        return context

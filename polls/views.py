from django.template import loader
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
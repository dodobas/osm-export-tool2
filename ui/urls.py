from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = patterns('ui.views',
    url(r'^$', TemplateView.as_view(template_name='ui/index.html'), name='index'),
)
from django.urls import include, path

from .views import troop, scouts, parents, leaders
from django.views.generic import TemplateView


urlpatterns = [
    path('', troop.home, name='home'),

    path('scouts/', include(([
        path('', TemplateView.as_view(
            template_name='scout_landing.html'), name='landing'),
    ], 'troop'), namespace='scouts')),

    path('parents/', include(([
        path('', TemplateView.as_view(
            template_name='parent_landing.html'), name='landing'),
    ], 'troop'), namespace='parents')),

    path('leaders/', include(([
        path('', TemplateView.as_view(
            template_name='leader_landing.html'), name='landing'),
    ], 'troop'), namespace='leaders')),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_prop', views.all_prop, name='all_prop'),
    path('all_prop/<int:p_id>', views.all_details, name='all_details'),
    path('add_prop', views.add_prop, name='add_prop'),
    path('filter_prop', views.filter_prop, name='filter_prop'),
    path('remove', views.remove, name='remove'),
    path('remove/<int:p_id>', views.remove, name='remove'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
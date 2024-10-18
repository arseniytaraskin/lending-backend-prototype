from django.urls import path
from .views import ContentBlockList, get_content

urlpatterns = [
    path('blocks/', ContentBlockList.as_view(), name='block-list'),
    path('get_content/', get_content, name='get_content')
]

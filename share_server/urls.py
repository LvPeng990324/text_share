from django.urls import path
from django.views.generic import RedirectView
from .views import index
from .views import text_detail
from .views import create_text
from .views import delete_text
from .views import top_text
from .views import no_top_text


urlpatterns = [
    # 跳转到index
    path('', RedirectView.as_view(url='index/')),
    path('index/', index, name='index'),
    path('text_detail/<text_id>/', text_detail, name='text_detail'),
    path('create_text/', create_text, name='create_text'),
    path('delete_text/', delete_text, name='delete_text'),
    path('top_text/', top_text, name='top_text'),
    path('no_top_text/', no_top_text, name='no_top_text'),
]

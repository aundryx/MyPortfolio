from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
import myapp.views

urlpatterns = [
    re_path(r'^$', myapp.views.index, name='home-page'),
    re_path(r'^home$', myapp.views.index, name='home-page'),
    re_path(r'^portfolio$', myapp.views.Portfolio, name='portfolio-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, TemplateView
from photos.models import Picture

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Picture.objects.all().order_by("created")[:6],
    							template_name="index.html")),
    url(r'^about/$', ListView.as_view(queryset=Picture.objects.all().order_by("created")[:6],
                                template_name="about.html")),
    url(r'^pic_detail/(?P<pk>\d+)$', DetailView.as_view(model=Picture,
    							template_name="details.html")),
	url(r'^galleri/$',  ListView.as_view(queryset=Picture.objects.all().order_by("-created")[:20],
    							template_name="galleri.html")),
    url(r'^galleric/$', ListView.as_view(queryset=Picture.objects.all().order_by("-created")[:20],
                                template_name="galleric.html")),
    url(r'^gallerik/$', ListView.as_view(queryset=Picture.objects.all().order_by("-created")[:20],
                                template_name="gallerik.html")),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    url(r'^photos/addPhoto/$', 'photos.views.add_photos_view', name='auth_add_photo'),
    url(r'^userGallery/$',  ListView.as_view(queryset=Picture.objects.all().order_by("-created")[:20],
                                template_name="userGalleri.html")),

)
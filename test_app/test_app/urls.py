from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    # Documentation URL
    url(
        r'^docs/',
        include_docs_urls(
            title='REST APIs Documentation',
            permission_classes=(permissions.AllowAny,),
        )
    ),
    # Chaining Accounts URLs
    url(
        r'^accounts/',
        include('accounts.urls')
    ),
]

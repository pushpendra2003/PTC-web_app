from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task, UserProfile, Click, Withdrawal

admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(Click)
admin.site.register(Withdrawal)

from django.contrib.admin.sites import site
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

class MyAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom-view/', self.admin_view(self.custom_view))
        ]
        return custom_urls + urls

    def custom_view(self, request):
        # Custom logic here
        context = {
            'title': 'Custom View',
            'message': 'Hello, this is a custom admin view!'
        }
        return render(request, 'admin/custom_view.html', context)

admin_site = MyAdminSite(name='myadmin')

from .models import Task, Withdrawal

admin_site.register(Task)
admin_site.register(Withdrawal)

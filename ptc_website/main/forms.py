
from captcha.fields import ReCaptchaField
from django import forms
from .models import Task, Withdrawal

class TaskForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Task
        fields = ['task_type', 'description', 'reward']

class WithdrawalForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Withdrawal
        fields = ['amount']


from django.contrib import admin
from .models import Task, Withdrawal
from .forms import TaskForm, WithdrawalForm

class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    list_display = ('task_type', 'description', 'reward')
    search_fields = ('description',)
    list_filter = ('task_type',)

class WithdrawalAdmin(admin.ModelAdmin):
    form = WithdrawalForm
    list_display = ('user', 'amount', 'status')
    list_filter = ('status',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)



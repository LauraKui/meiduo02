from django.shortcuts import render
from django.views.generic import View

# 注册

class Register(View):
    def get(self, request):
        """返回注册页面"""
        return render(request, 'register.html')

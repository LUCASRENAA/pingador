from django.shortcuts import render
import os
# Create your views here.

def pingar(request,ip):
    command = f'ping -c 1 {ip}'
    os.system(command)
    return render(request,'core/index.html',{'ip':ip})
from django.shortcuts import render
import itertools
from base_tools import function



def home(request):
    result = None
    if request.method == 'POST':
        nums = [
            int(request.POST.get('num1')),
            int(request.POST.get('num2')),
            int(request.POST.get('num3')),
            int(request.POST.get('num4')),
            int(request.POST.get('num5'))
        ]
        result = function(nums,15)
    return render(request, 'calculator/home.html', {'result': result})

def set(request):
    result = None
    if request.method == 'POST':
        target = int(request.POST.get('target'))
        nums=[]
        for i in range(1,6):
            num=request.POST.get(f'num{i}')
            if num:
                nums.append(int(num))


        result = function(nums,target)
    return render(request, 'calculator/set.html', {'result': result})
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic={'text':'hello world','number':100}
    return render(request,'fourapp/index.html',context_dic)

def other(request):
    return render(request,'fourapp/other.html')

def relative(request):
    return render(request,'fourapp/relative_url.html')

def inher(request):
    return render(request,'fourapp/inher.html')
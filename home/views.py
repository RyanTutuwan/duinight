from django.shortcuts import render
def index(request):
    template_data={}
    template_data['title'] = 'DUI NIGHT'
    return render(request, 'home/index.html', {'template_data' : template_data})

def guide(request):
    template_data={}
    template_data['title'] = 'GUIDE'
    return render(request, 'home/guide.html', {'template_data' : template_data})
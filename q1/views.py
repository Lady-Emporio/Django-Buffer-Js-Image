from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from q1.models import SaveImage

from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = SaveImage
        fields = '__all__'


def index(request):
    if request.method == 'POST':
        formset = ArticleForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
        else:
            return render(request,"WebPage1.html",{"message":"not valid"})
    else:
        formset = ArticleForm()
    return render(request,"WebPage1.html",{"form":formset})

def detail(request,pk):
    n=SaveImage.objects.get(pk=pk)


    if request.method == 'POST':
        formset = ArticleForm(request.POST, request.FILES,instance=n)
        if formset.is_valid():
            formset.save()
            # do something.
        else:
            return render(request,"WebPage1.html",{"message":"not valid"})
    else:
        formset = ArticleForm(instance=n)
    return render(request,"WebPage1.html",{"form":formset})

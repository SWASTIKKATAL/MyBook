from django.shortcuts import render

from notes.forms import NotesForm
from . models import Notes
# Create your views here.
def create_notes(request):
    context ={}
    form = NotesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,"create_view.html",context)    



def getall_notes(request):
    allnotes=Notes.objects.all()
    
    context={"data":allnotes}
    print(allnotes)
    return render(request,'all_notes.html',context)

def detail_view(request,id):
    context= {}
    context["data"] = Notes.objects.get(id = id) 
    return render(request, "detail_view.html", context)


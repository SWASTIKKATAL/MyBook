from django.shortcuts import render

from .forms import UserForm
from .models import Users

# Create your views here.
def create_user(request):
    context ={}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,"create_user.html",context)   

def getall_users(request):
    allusers=Users.objects.all()

    context={"data":allusers}
    print(allusers)
    return render(request,"all_users.html",context)


def login_user(request,id):
    context= {}
    context["data"] = Users.objects.get(id = id) 
    return render(request, "detailed_view.html", context)
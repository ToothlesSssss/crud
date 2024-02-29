from django.shortcuts import render , redirect
from.models import Detail
# Create your views here.


def index(request):
  data=Detail.objects.all()
  print(data)
  context={"data":data}
  return render(request, 'index.html',context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        print(name, email, tel)
        query = Detail(name=name, email=email, tel=tel)
        query.save()
        return redirect("/")
    
    return render(request, 'index.html')



def updateData(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        edit=Detail.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.tel=tel
        edit.save()
        return redirect("/")
  
  
    d=Detail.objects.get(id=id)
   
    context={"d":d}
    return render(request, 'edit.html',context)


def deleteData(request,id):
  
    d=Detail.objects.get(id=id)
    d.delete()
    return redirect("/")



def edit(request):
  return render(request, 'edit.html')


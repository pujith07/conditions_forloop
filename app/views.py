from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':200,'b':300,'c':40}
    return render(request,'conditions.html',d)
def loops(request):
    d={'p':['name:pujith','gender:male','age:22'],'dhoni':['name:MS Dhoni','role:Right hand batsman','age:40']}
    return render(request,'loops.html',d)
def dhoni(request):
    d={'dhoni':['name:MS Dhoni','role:Right hand batsman','age:40']}
    return render(request,'loops.html',d)
def kholi(request):
    d={'kholi':['Name:Virat Kholi','Role:Right hand batsman','age:33']}
    return render(request,'loops.html',d)
def rohit(request):
    d={'rohit':['Name:Rohit Sharma','role:Right hand batsman','age:35']}
    return render(request,'loops.html',d)
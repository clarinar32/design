from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def portfolio(request):
    return render(request,"portfolio.html")
def contact(request):
     return render(request,"contact.html")
def service(request):
     return render(request,"service.html")
def about(request):
    return render(request,"about.html")

from django.shortcuts import render

def index(request):
    #defining random variable
    number = 6
    thing = "Thing name"
    #passing the variable to the template
    return render(request,'index.html',{
    'number': number,
    'thing':thing,
    })
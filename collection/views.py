from django.shortcuts import render,redirect
from collection.models import Thing
from collection.forms import ThingForm
import string

def index(request):
    things = Thing.objects.all()
    return render(request,'index.html',{
    'things' : things,
    }) 

def thing_detail(request,slug):
    thing = Thing.objects.get(slug=slug)
    return render(request,'things/thing_detail.html',{
        'thing' : thing,
        })

def edit_thing(request,slug):
    thing = Thing.objects.get(slug=slug)
    form_class = ThingForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail',slug=thing.slug)
    else:
        form = form_class(instance=thing)

    return render(request,'things/edit_thing.html', {
        'thing':thing,
        'form':form,
        })

def browse_by_name(request,initial=None):
    lowercaseletters = string.ascii_lowercase
    if initial:
        things = Thing.objects.filter(name__startswith=initial)
        things = things.order_by('name')

    else:
        things = Thing.objects.all().order_by('name')

    return render(request,'browse/browse_by_name.html',{
        'things': things,
        'initial':initial,
        'letters':lowercaseletters,
        })

from django.shortcuts import render
from django.http import HttpResponse
from. models import Property, Contact
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def all_prop(request):
    props = Property.objects.all()
    context = {
        'props': props
    }
    return render(request, 'myapp/all_prop.html', context)

def all_details(request, p_id):
    i = Property.objects.get(pk=p_id)
    return render(request, 'myapp/details.html', {'i': i})


def add_prop(request):
    if request.method == 'POST':
        retailer = request.POST['retailer']
        title = request.POST['title']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        code = int(request.POST['code'])
        description = request.POST['description']
        price = int(request.POST['price'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = int(request.POST['bathrooms'])
        garage = int(request.POST['garage'])
        sqft = int(request.POST['sqft'])
        lot_size = int(request.POST['lot_size'])
        photo_main = request.POST['photo_main']
        photo_1 = request.POST['photo_1']
        photo_2 = request.POST['photo_2']
        photo_3 = request.POST['photo_3']
        photo_4 = request.POST['photo_4']
        photo_5 = request.POST['photo_5']
        photo_6 = request.POST['photo_6']
        new_prop = Property(retailer=retailer, title=title, address=address, city=city, state=state,code=code, description=description, price=price, bedrooms=bedrooms,bathrooms=bathrooms,
                           garage=garage, sqft=sqft, lot_size=lot_size,photo_main=photo_main,photo_1=photo_1, photo_2=photo_2, photo_3=photo_3, photo_4=photo_4, photo_5=photo_5, photo_6=photo_6,
                            email=email, contact=contact)
        new_prop.save()
        return HttpResponse('Property added Successfully')
    elif request.method == 'GET':
        return render(request, 'myapp/add_prop.html')
    else:
        return HttpResponse("An Exception Occured Property")

def remove(request,p_id=0):
    if p_id:
        try:
            prop_to_be_removed = Property.objects.get(id=p_id)
            prop_to_be_removed.delete()
            return HttpResponse("Property Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    prop = Property.objects.all()
    context = {
            'prop': prop
        }
    return render(request, 'myapp/remove.html',  context)


def filter_prop(request):
    if request.method == 'POST':
        price = request.POST['price']
        city = request.POST['city']
        state = request.POST['state']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        props = Property.objects.all()

        if price:
            props = props.filter(price__lte=price)

        if city:
            props = props.filter(city__icontains=city)

        if state:
            props = props.filter(state__icontains=state)

        if bedrooms:
            props = props.filter(bedrooms__icontains=bedrooms)


        if bathrooms:
            props = props.filter(bathrooms__icontains=bathrooms)

        context = {
            'props': props
        }
        return render(request, 'myapp/all_prop.html', context)

    elif request.method == 'GET':
        return render(request, 'myapp/filter_prop.html')
    else:
        return HttpResponse('An Exception Occurred')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']
        cont = Contact(fname=fname, lname=lname, email=email,message=message)
        cont.save()
        return HttpResponse('Thank You')
    else:
        # if request method is get
        return render(request, 'myapp/contact.html')

def about(request):
    return render(request, 'myapp/about.html')
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from .forms import *
from django.contrib import messages


def admin_t(request):
    return render(request, 'admin_t.html')



def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    images = Image.objects.all()
    profiessionalchefs = Proffesionalchef.objects.all() 
    ourgallerys = Ourgallery.objects.all()
    contacts = Contact.objects.all()
    testimonals = Testimonial.objects.all()
    return render(request, 'index.html', context={
        'categories': categories,
        'products': products,
        'images': images,
        'profiessionalchefs': profiessionalchefs,
        'ourgallerys': ourgallerys,
        'contacts': contacts,
        'testimonals': testimonals,
    })

def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!')
            return redirect('book_table') 
    else:
        form = ReservationForm()

    return render(request, 'index.html', {'form': form})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})



def contact_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        
        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()  

        
        return render(request, 'contact.html', {'sent': True})

    return render(request, 'contact.html')

from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()

    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains = search_input)
    else:
        contacts = Contact.objects.all() 
        search_input = ""
    return render(request, 'contact/index.html', {'contacts': contacts, 'search_input': search_input})


def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            phone_number = request.POST['phone-number'],
            email = request.POST['email'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/contact')
    return render(request, 'contact/new.html')


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.phone_number = request.POST['phone-number']
        contact.email = request.POST['e-mail']
        contact.address = request.POST['address']
        
        contact.save()
        return redirect('/contact/contact_profile/' + str(contact.id))

    return render(request, 'contact/edit.html', {'contact': contact})


def profileContact(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact/contact-profile.html', {'contact': contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/contact')
    return render(request, 'contact/delete.html', {'contact': contact})
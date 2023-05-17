from django.shortcuts import render, redirect
from travelapp import models


# Create your views here.


def Register(request):
       
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        destination = request.POST['destination']
        travelers = request.POST['travelers']
        budget = request.POST['budget']
        currency = request.POST['currency']

        travel_registration = models.FormSubmission(
            name=name,
            email=email,
            destination=destination,
            travelers=travelers,
            budget=budget,
            currency=currency
        )
        print(travelers)
        travel_registration.save()
        return redirect('register')
    else:
        return render(request, "Register.html") 
  


def Lists(request):

    submissions = models.FormSubmission.objects.all()
    return render(request, 'lists.html', {'submissions': submissions})
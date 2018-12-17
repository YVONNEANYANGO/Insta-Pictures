from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image,NewsLetterRecipients
# from datetime as dt
from django.http import Http404
from .forms import NewsLetterForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/pics.html", {{"image":image}})


def photos_today(request):
    date = dt.date.today()
    photos = Image.todays_photos()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('photos_today')

    else:
        form = NewsLetterForm()
    
    return render(request, 'all-photos/today-photos.html', {"date": date,"uploads":uploads,"letterForm":form})

    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_profile_user_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id =image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image"})

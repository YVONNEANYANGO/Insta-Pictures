from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image,NewsLetterRecipients,Comment
# from datetime as dt
from django.http import Http404
from .forms import NewsLetterForm,forms
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='accounts/login/')
def welcome(request):
    images = Image.objects.all()

    comments = Comment.objects.all()

    
    return render(request, 'welcome.html' ,{"images":images,"comments":comments,"form":forms })


@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/profile.html", {{"image":image}})


def new_image(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile = Current_user
            image.save()
        return redirect('index')
    else:
        form=NewImageForm()
    return render(request, 'new_image.html', {"form":form})


def photos_today(request):
    date = dt.date.today()
    images = Image.todays_photos()

    form = NewsLetterForm()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('welcome.html')
            print('valid')

    else:
        form = NewsLetterFor

    forms = Form.objects.all()
  
    
    return render(request, 'all-photos/welcome.html', {"date": date,"images":images, "Letterform":form})

    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Returning the actual day of the week}

    day = days[day_number]
    return day


def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_profile = request.GET.get("profile")
        search_profile = profile.search_by_profile(search_profile)
        message = f"{search_profile}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message}) 


def profile(request):
    current_user=request.user
    photos=Image.objects.filter(profile=current_user)
    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request, 'profile.html', {"photos":photos, "profile":profile})


@login_required(login_url='/accounts/login')
def upload_image(request):
    if request_method == 'POST':
        uploadform.is_valid()
        upload = uploadform.save(commit=False)
        upload.profile = request.user.profile
        upload.save()
        return redirect('profile', username=request.user)

    else:
        uploadform = ImageForm()

        return render(request, 'all-photos/profile.html', {'uploadform':uploadform})




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

    form = NewsLetterForm()

    # forms = Form.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('photos_today')

    else:
        form = NewsLetterForm()

    return render(request, 'welcome.html' ,{"images":images,"comments":comments, "LetterForm":form})


@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/pics.html", {{"image":image}})


def photos_today(request):
    date = dt.date.today()
    images = Image.todays_photos()
    form = NewsLetterForm()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('photos_today')

    else:
        form = NewsLetterForm()
    
    return render(request, 'all-photos/comments.html', {"date": date,"images":images,"letterForm":form, "form":form})

    

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Returning the actual day of the week}

    day = days[day_number]
    return day


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_profile = request.GET.get("image")
        search_image = Image.search_by_profile_user(search_profile)
        message = f"{search_profile}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

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



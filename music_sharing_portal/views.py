from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from Service.models import ServiceUser
from Service.models import Song
from Service.models import SharedSong
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        user_data = ServiceUser.objects.filter(username=email).values()
        if not user_data:
            print("invalid email or password")
            data = {'message': "inavlid email or password"}
            return render(request, "index.html", data)
        else:

            dictdata = user_data[0]
            d_password = dictdata['password']
            print(password)
            if d_password == password:
                login(request, user)
                return redirect('songs')
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        my_user = User.objects.create_user(email, name, password)

        en = ServiceUser(name=name, username=email,
                         gender=gender, password=password)

        print(name, email, gender, password)
        en.save()
        my_user.save()
        return redirect('home')

    return render(request, "signup.html")


@login_required(login_url='/')
def songs(request):
    data = Song.objects.filter(privacy="public")
    songdata = {"songs": data}
    return render(request, "user/index.html", songdata)


@login_required(login_url='/')
def shared_songs(request):

    user_email = request.user.username
    print(user_email)
    data = SharedSong.objects.filter(email=user_email).values()
    print(data)
    #dictdata = data[0]
    # print(dictdata)
    #songname = dictdata['songName']
    #song_data = Song.objects.filter(title=songname)

    songdata = {"songs": data}
    return render(request, "user/sharedsongs.html", songdata)


@login_required(login_url='/')
def upload_song(request):
    if request.method == 'POST':
        song_title = request.POST.get('title')
        singer_name = request.POST.get('singer')
        song = request.FILES['song']
        song_img = request.FILES['photo']
        song_privacy = request.POST.get('user-privacy')
        user_email = request.POST.get('userEmail')
        en = Song(title=song_title, singer_name=singer_name, song=song,
                  songs_image=song_img, privacy=song_privacy, users_email=user_email)
        en.save()

        if (user_email != None):
            username = request.user.email

            email = user_email.split()
            for e in email:
                db = SharedSong(email=e, songName=song_title, sharedBy=username, singer_name=singer_name, song=song,
                                songs_image=song_img)
                db.save()

    return render(request, "user/upload-music.html")


def logout_page(request):
    logout(request)
    return redirect('login')

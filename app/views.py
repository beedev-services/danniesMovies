from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import *
import bcrypt


def index(request):
    if 'user_id' not in request.session:
        users= User.objects.all().values()
        dvds = Dvd.objects.order_by('title')
        cds = Cds.objects.order_by('albumTitle')
        genres = Topic.objects.all().values().order_by('topic')
        films = Film.objects.all().values()
        context = {
            'users': users,
            'dvds': dvds,
            'cds': cds,
            'films': films,
            'genres': genres,
        }
        return render(request, 'index.html', context)
    else:
        users= User.objects.all().values()
        user = User.objects.get(id=request.session['user_id'])
        dvds = Dvd.objects.order_by('title')
        cds = Cds.objects.order_by('albumTitle')
        genres = Topic.objects.all().values().order_by('topic')
        films = Film.objects.all().values()
        context = {
            'users': users,
            'user': user,
            'dvds': dvds,
            'cds': cds,
            'films': films,
            'genres': genres,
        }
        print('films', films)
        print('genres', genres)
        return render(request, 'logged/dashboard.html', context)

def allMovies(request):
    if 'user_id' not in request.session:
        users= User.objects.all().values()
        dvds = Dvd.objects.order_by('title')
        films = Film.objects.all().values()
        genres = Topic.objects.all().values().order_by('topic')
        context = {
            'users': users,
            'dvds': dvds,
            'films': films,
            'genres': genres,
        }
        return render(request, 'movies.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        users= User.objects.all().values()
        dvds = Dvd.objects.order_by('title')
        films = Film.objects.all().values()
        genres = Topic.objects.all().values().order_by('topic')
        context = {
            'users': users,
            'user': user,
            'dvds': dvds,
            'films': films,
            'genres': genres,
        }
        return render(request, 'logged/dashMovies.html', context)

def viewMovie(request, dvd_id):
    if 'user_id' not in request.session:
        users=User.objects.all().values()
        dvd=Dvd.objects.get(id=dvd_id)
        genres = Topic.objects.all().values().order_by('topic')
        films = Film.objects.all().values()
        context = {
            'users': users,
            'dvd': dvd,
            'films': films,
            'genres': genres,
        }
        return render(request, 'viewMovie.html', context)
    else:
        users=User.objects.all().values()
        user=User.objects.get(id=request.session['user_id'])
        dvd=Dvd.objects.get(id=dvd_id)
        genres = Topic.objects.all().values().order_by('topic')
        films = Film.objects.all().values()
        context = {
            'users': users,
            'user': user,
            'dvd': dvd,
            'films': films,
            'genres': genres,
        }
        return render(request, 'logged/dashViewMovie.html', context)

def allMusic(request):
    if 'user_id' not in request.session:
        users= User.objects.all().values()
        cds = Cds.objects.order_by('albumTitle')
        context = {
            'users': users,
            'cds': cds,
        }
        return render(request, 'music.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        users= User.objects.all().values()
        cds = Cds.objects.order_by('albumTitle')
        context = {
            'users': users,
            'user': user,
            'cds': cds,
        }
        return render(request, 'logged/dashMusic.html', context)

def viewMusic(request, cds_id):
    if 'user_id' not in request.session:
        users=User.objects.all().values()
        cd=Cds.objects.get(id=cds_id)
        context = {
            'users': users,
            'cd':cd,
        }
        return render(request, 'viewMusic.html', context)
    else:
        users=User.objects.all().values()
        user=User.objects.get(id=request.session['user_id'])
        cd=Cds.objects.get(id=cds_id)
        context = {
            'users': users,
            'user': user,
            'cd':cd,
        }
        return render(request, 'logged/dashViewMusic.html', context)

def theAdmin(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else: 
        user = User.objects.get(id=request.session['user_id'])
        movies = Dvd.objects.all().values().order_by('-id')
        musics = Cds.objects.all().values()
        genres = Topic.objects.all().values().order_by('topic')
        films = Film.objects.all().values()
        context = {
            'user': user,
            'movies': movies,
            'musics': musics,
            'genres': genres,
            'films': films,
        }
        print("films: ", films)
        return render(request, 'logged/theAdmin.html', context)

def logReg(request):
    if 'user_id' not in request.session:
        context = {
            "user": User.objects.all().values()
        }
        return render(request, 'logReg.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
    return redirect('/theAdmin/')

def register(request):
    if request.method == 'GET':
        return redirect('/logReg/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    hashedKey = bcrypt.hashpw(request.POST['adminKey'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        adminKey = hashedKey,
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/')

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/logReg/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/logReg/')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def createGenre(request):
    Topic.objects.create(
        topic = request.POST['topic']
    )
    messages.error(request, 'Genre Created')
    return redirect('/theAdmin/')

def createDvd(request):
    Dvd.objects.create(
        title = request.POST['title'],
        actors = request.POST['actors'],
        year = request.POST['year'],
        misc = request.POST['misc'],
        user_id = request.POST['user']
    )
    messages.error(request, 'Movie created!')
    return redirect('/theAdmin/')

def addMovieGenre(request):
    Film.objects.create(
        dvd_id = request.POST['dvd'],
        genre_id = request.POST['genre']
    )
    messages.error(request, 'Genre added')
    return redirect('/theAdmin/')

def createCds(request):
    Cds.objects.create(
        albumTitle = request.POST['albumTitle'],
        artist = request.POST['artist'],
        year = request.POST['year'],
        user_id = request.POST['user']
    )
    messages.error(request, 'Cd Created!')
    return redirect('/theAdmin/')

def updateDvd(request, dvd_id):
    toUpdate = Dvd.objects.get(id=dvd_id)
    toUpdate.title = request.POST['title']
    toUpdate.actors = request.POST['actors']
    toUpdate.year = request.POST['year']
    toUpdate.misc = request.POST['misc']
    toUpdate.save()
    messages.error(request, "DVD Updated")
    return redirect('/theAdmin/')

def updateTopic(request, topic_id):
    toUpdate = Topic.objects.get(id=topic_id)
    toUpdate.topic = request.POST['topic']
    toUpdate.save()
    messages.error(request, 'Genre updated')
    return redirect('/theAdmin/')

def updateCds(request, cds_id):
    toUpdate = Cds.objects.get(id=cds_id)
    toUpdate.albumTitle = request.POST['albumTitle']
    toUpdate.artist = request.POST['artist']
    toUpdate.year = request.POST['year']
    toUpdate.save()
    messages.error(request, 'CD Updated')
    return redirect('/theAdmin/')

def deleteDvd(request, dvd_id):
    toDelete = Dvd.objects.get(id=dvd_id)
    toDelete.delete()
    messages.error(request, "DVD removed")
    return redirect('/theAdmin/')

def deleteTopic(request, topic_id):
    toDelete = Topic.objects.get(id=topic_id)
    toDelete.delete()
    messages.error(request, "Genre deleted")
    return redirect('/theAdmin/')

def deleteCds(request, cds_id):
    toDelete = Cds.objects.get(id=cds_id)
    toDelete.delete()
    messages.error(request, 'CD Removed')
    return redirect('/theAdmin/')
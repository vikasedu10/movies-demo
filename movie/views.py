from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

from movie.forms import SignupForm, DirectorForm, MovieForm, StudioForm
from django.views import generic

from movie.models import Director, Genre, NewMovie, Studio


def index(request):
    return render(request, "movie/index.html")


@transaction.atomic
@login_required
def create_new_director(request):
    form = DirectorForm(request.POST or None)

    if form.is_valid():
        form_obj = form.save()
        return redirect('director', form_obj.id)

    params = {
        'form': form,
    }
    return render(request, 'movie/new-director.html', params)


class GenreCreate(generic.CreateView):
    model = Genre
    template_name = 'movie/new-genre.html'
    fields = ("title",)
    success_url = '/'


@transaction.atomic
@login_required
def new_movie(request):
    if request.POST:
        form = MovieForm(request.POST, request.FILES or None)
    else:
        form = MovieForm()

    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.image = request.FILES['image']
        form_obj.release_date = datetime.today()
        form_obj.save()
        form.save_m2m()
        return redirect('movie', form_obj.id)

    params = {
        'form': form,
    }
    return render(request, 'movie/new-movie.html', params)


class MoviesList(generic.ListView):
    model = NewMovie
    template_name = 'movie/movies.html'
    context_object_name = "movies"
    ordering = ['-timestamp']


class MovieDetail(generic.DetailView):
    model = NewMovie
    template_name = "movie/movie.html"
    context_object_name = "movie"


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                return HttpResponse("Invalid username & password")

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


class DirectorList(generic.ListView):
    model = Director
    template_name = 'movie/directors.html'
    context_object_name = "directors"


class DirectorDetail(generic.DetailView):
    model = Director
    template_name = "movie/director.html"
    context_object_name = "director"


@transaction.atomic
@login_required
def new_studio(request):
    form = StudioForm(request.POST or None)

    if form.is_valid():
        form_obj = form.save(commit=False)
        # slug = form_obj.cleaned_data['title']
        form.save()
        return redirect('studio', form_obj.id)

    params = {
        'form': form,
    }
    return render(request, 'movie/new-studio.html', params)


class StudioList(generic.ListView):
    model = Studio
    template_name = 'movie/studios.html'
    context_object_name = 'studios'


class StudioDetail(generic.DetailView):
    model = Studio
    template_name = 'movie/studio.html'
    context_object_name = 'studio'


class GenreList(generic.ListView):
    model = Genre
    template_name = "movie/genres.html"
    context_object_name = "genres"

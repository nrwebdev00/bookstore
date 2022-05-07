from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from utlis.recipesAPI import RecipesAPI

from .models import Profile, Favorites
from utlis.tagsAPI import TagsAPI
 
def users(request):

    context = {
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
    }

    return render(request, 'users/users.html', context)

@login_required
def profile(request):
    profile = Profile.objects.get(userName=request.user)
    favorites = Favorites.objects.filter(owner=profile)
    context = {
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
        'profile':profile,
        'favorites':favorites,
    }

    return render(request, 'users/profile.html', context)

@login_required
def delFavorite(request, pk):
    favorite = Favorites.objects.get(id=pk)
    favorite.delete()
    return redirect('users-profile')

@login_required
def addFavorite(request, id):
    recipe = RecipesAPI(id).SingleRecipe()
    profile = Profile.objects.get(userName=request.user)
    Favorites.objects.create(owner=profile, recipeName=recipe['name'], recipeId=recipe['id'])
    return redirect('recipes-single', id)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('pages-home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username Or Password is Incorrect')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pages-home')
        else:
            messages.error(request, 'Username Or Password is Incorrect')

    context = {
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
    }

    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')

def registerUser(request):

    if request.user.is_authenticated:
        return redirect('pages-home')

    if request.method == 'POST':
        user = request.POST
        userName = user['userName']
        email = user['email']
        password = user['password']

        if User.objects.filter(username=userName).exists() == False:
            newUser = User.objects.create_user(userName, email, password)
            newUser.save()
            messages.success(request, "New User was Register, Please Login")
            return redirect('login')
        else:
            messages.error(request, "User Name already exists")
            return redirect('login')
        


    context = {
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
    }

    return render(request, 'users/register.html', context)
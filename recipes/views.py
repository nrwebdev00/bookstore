from string import ascii_letters, digits
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth import authenticate

from utlis.tagsAPI import TagsAPI
from utlis.recipesAPI import RecipesAPI, RecipesList, RecipesSearch
from users.models import Favorites

def recipesList(request, tag, page):
    list = RecipesList(tag).ListRecipes()
    displayTag = tag.replace("_", " ").title()
    page_number = page
    paginator = Paginator(list, 9)
    list = paginator.page(page_number)
    total_pages = paginator.num_pages
    

    context = {
        'displayTag':displayTag,
        'tag':tag,
        'list':list,
        'page_num': page_number,
        'total_pages': total_pages,
        'page_name': 'recipes-list',
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
        'checkList': RecipesList(tag).CheckIfListReturns(),
    }
    return render(request, 'recipes/recipesList.html', context)

def recipesListString(request, q, page):
    list = RecipesSearch(q).SearchList()
    displayTag = q.replace("-", " ").title()
    page_number = page
    paginator = Paginator(list, 9)
    list = paginator.page(page_number)
    total_pages = paginator.num_pages 


    context = {
        'list':list,
        'tag': q,
        'displayTag': displayTag,
        'page_num': page_number,
        'total_pages': total_pages,
        'page_name': 'recipes-search',
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
        }

    return render(request, 'recipes/recipesListString.html', context)

def recipes(request):

    context = {
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
    }
    return render(request, 'recipes/recipes.html', context)


def recipe(request, pk):
    if request.user.is_authenticated:
        authUser = True
    else:
        authUser = False
    
    tagList = RecipesAPI(pk).TagList()
    
    try:
        favorite = Favorites.objects.get(recipeId=pk)
    except:
        favorite = 'None'

    print(favorite)
     

    context = {
        'authUser': authUser,
        'favorite': favorite,
        'tagList': tagList,
        'recipe':RecipesAPI(pk).SingleRecipe(), 
        'ingredients': RecipesAPI(pk).Ingredients, 
        'instructions': RecipesAPI(pk).Instructions, 
        'nutrition' : RecipesAPI(pk).Nutrition(),
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'), 
    }
    return render(request, 'recipes/singleRecipe.html', context)

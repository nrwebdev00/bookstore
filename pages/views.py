from utlis.tagsAPI import TagsAPI
from utlis.recipesAPI import RecipesAPI, RecipesList
from django.shortcuts import render



def home(request):


    heroRecipe = RecipesAPI(7522).SingleRecipe()
    heroList = RecipesList('easter', size=6).ListRecipes()

    context = {
        'occasionList': TagsAPI(12).List('occasion') ,
        'cuisineList': TagsAPI(12).List('cuisine'),
        'dietList': TagsAPI(12).List('dietary'),
        'holidayList': TagsAPI(12).List('holiday'),
        'methodList': TagsAPI(12).List('method'),
        'heroRecipe': heroRecipe,
        'heroList': heroList,
        }

    return render(request, 'pages/home.html', context)

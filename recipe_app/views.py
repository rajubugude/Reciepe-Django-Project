from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.
def recipe(request):
    if request.method == 'POST' :
        # recipe_name = request.POST['recipe_name']
        # recipe_desc = request.POST['recipe_desc']
        # recipe_img = request.FILES['recipe_img']


        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')
        new_recipe = Recipe(recipe_name = recipe_name,recipe_desc = recipe_desc,recipe_img = recipe_img )
        new_recipe.save()

        return redirect('/')
    
    recipes = Recipe.objects.all()

    #for search
    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))
    context = {
        'recipes':recipes
    }
    context = {
        'recipes':recipes
    }

    return render(request,'recipe.html',context)


def remove_recipe(request,recipe_id):
    recipe_to_be_removed = Recipe.objects.get(id=recipe_id)
    recipe_to_be_removed.delete()
    return redirect('/')


def update_recipe(request,recipe_id):
    queryset = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST' :
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')
       
        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_img:
            queryset.recipe_img = recipe_img
        queryset.save()

        return redirect('/')

    context = {
        'recipe':queryset
    }

    return render(request,'update_recipe.html',context)



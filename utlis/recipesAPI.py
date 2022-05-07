import requests
import re

APIKEY = "65c425a0f1mshc61460168d6ff78p1c4feejsn34a46948cd22"

class RecipesAPI:

    def __init__(self, id):
        self.id = id
        self.url = "https://tasty.p.rapidapi.com/recipes/get-more-info"
        self.querystring = {"id":self.id}
        self.headers = {
            "X-RapidAPI-Host": "tasty.p.rapidapi.com",
            "X-RapidAPI-Key": APIKEY
        }

    def SingleRecipe(self):
        response = requests.request("GET", self.url, headers= self.headers, params=self.querystring)
        res = response.json()
        return(res)

    def Instructions(self):
        recipe = self.SingleRecipe()
        instructions = recipe['instructions']
        return instructions

    def Nutrition(self):
        recipe = self.SingleRecipe()
        nutrition = recipe['nutrition']
        if nutrition == 'update_at':
            nutrition.pop('update_at')
        return nutrition

    def TagList(self):
        recipe = self.SingleRecipe()
        tags = recipe['topics']
        return tags
    

    def Ingredients(self):
        sections = []
        components = []
        ingredients = []
        recipe = self.SingleRecipe()

        for i in recipe['sections']:
            sections.append(i)
        
        for i in sections:
            components.append(i['components'])
        
        for x in components:
            for i in x:
                ingredients.append(i['raw_text'])

        return ingredients

# Search by tags all ready set my tasty API
class RecipesList:

    def __init__(self, tag, size=900, fromPos=0):
        self.tag = tag
        self.size = size
        self.fromPos = fromPos
        self.url = "https://tasty.p.rapidapi.com/recipes/list"
        self.querystring = {"from":fromPos,"size":self.size,"tags":self.tag}

        self.headers = {
            "X-RapidAPI-Host": "tasty.p.rapidapi.com",
            "X-RapidAPI-Key": APIKEY
        }

    def CheckIfListReturns(self):
        response = requests.request("GET", self.url, headers= self.headers, params=self.querystring)
        res = response.json()
        count = res['count']
        if res['count'] == 0:
            return False
        else:
            return(count)

    def ListRecipes(self):
        response = requests.request("GET", self.url, headers= self.headers, params=self.querystring)
        res = response.json()
        list = res["results"]
        filterList = []

        # To have list return only recipes and remove anything else
        for i in list:
            valueTest = i['canonical_id'][:6]
            if valueTest == 'recipe':
                filterList.append(i)

        return(filterList)

# Search API via query string
class RecipesSearch:
    def __init__(self, q, size=900, fromPos=0):
        self.query = q
        self.size = size
        self.fromPos = fromPos
        self.url = "https://tasty.p.rapidapi.com/recipes/list"
        self.querystring ={ "from":self.fromPos,"size":self.size,"q":self.query}
        self.headers={
            "X-RapidAPI-Host": "tasty.p.rapidapi.com",
            "X-RapidAPI-Key": APIKEY
        }
    
    def SearchList(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        res = response.json()
        list = res['results']
        return list





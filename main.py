# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, jsonify
from firebase_admin import firestore, credentials, initialize_app
from bowlsRecipeScraper import BowlsRecipeScraper

app = Flask(__name__)

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
recipes_Ref = db.collection('recipes')

def get_user_ingreds(userID):
    try:
        # get ref to collection 'fav ingredients'
        ingred_ref = db.collection('fav ingredients')
        # get all documents where userID == userID
        user_ingred_ref = ingred_ref.where('userID', '==', userID).stream()
        # extract description from each document and add to list
        user_ingred = [ingred.to_dict()['description'] for ingred in user_ingred_ref]
    except:
        user_ingred = []

    return user_ingred # return list of user's ingredients

def comp_recipe_ingreds(recipeIngredients, ingredients):
    count = 0
    lenRecipeIngreds = len(recipeIngredients)
    # for each ingredient in recipe ingredients (long string)
    for ringredient in recipeIngredients:
        ringredient = ringredient.lower()
        # check if substring ingredient in target ingredients
        for ingredient in ingredients:
            ingredient = ingredient.lower()
            if ingredient in ringredient:
                count += 1
                break
        if (count / lenRecipeIngreds) >= 0.5: return True

    return (count / lenRecipeIngreds) >= 0.5

@app.route('/')
def hello_world():
    return 'Hello from Cookmate!'

@app.route('/list', methods=['GET'])
def read():
    try:
        recipe_id = request.args.get('id')
        if recipe_id:
            recipe_doc_ref = recipes_Ref.document(recipe_id)
            recipe_info = recipe_doc_ref.collection('info').document('info1').get()
            return jsonify(recipe_info.to_dict()), 200
        else:
            all_recipes = [doc.to_dict() for doc in recipes_Ref.stream()]
            return jsonify(all_recipes), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        # get user's id and recipe category
        category = request.args.get('category')
        userID = request.args.get('userID')
        user_ingreds = get_user_ingreds(userID) # get user's ingredients

        # scrape recipes from website based on category
        new_recipes = []
        scraper = BowlsRecipeScraper() # create scraper object
        links = scraper.get_links_one_page_bs(category)
        #print(links)

        # check if each recipe has at least 50% of user's ingredients
        for link in links:
            recipe = scraper.get_recipe(link, category)
            #recipe_ingreds = scraper.get_recipe_ingreds(link)
            if comp_recipe_ingreds(recipe['ingredients'], user_ingreds):
                #recipe = scraper.get_recipe(link, category)
                recipe['link'] = link # add link to recipe
                new_recipes.append(recipe) # add recipe to list if so

        return jsonify(new_recipes), 200 # return list of recipes
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/ingreds', methods=['GET'])
def get_ingreds():
    try:
        try:
            userID = request.args.get('userID')
            # get ref to collection 'fav ingredients'
            ingred_ref = db.collection('fav ingredients')
            # get all documents where userID == userID
            user_ingred_ref = ingred_ref.where('userID', '==', userID).stream()
            # extract description from each document and add to list
            user_ingred = [ingred.to_dict()['description'] for ingred in user_ingred_ref]
        except:
            user_ingred = []

        return jsonify(user_ingred), 200 # return list of user's ingredients
    except Exception as e:
        return f"An Error Occured: {e}"
    
@app.route('/recipe', methods=['GET'])
def get_recipe():
    try:
        link = request.args.get('link')
        category = request.args.get('category')
        scraper = BowlsRecipeScraper()
        recipe = scraper.get_recipe(link, category)
        return jsonify(recipe), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/links', methods=['GET'])
def get_links():
    try:
        category = request.args.get('category')
        scraper = BowlsRecipeScraper()
        links = scraper.get_links_one_page_bs(category)
        return jsonify(links), 200
    except Exception as e:
        return f"An Error Occured: {e}"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

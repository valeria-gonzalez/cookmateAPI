# Cookmate API 

Simple REST API that integrates Firestore and Flask.

## Features
It allows the user to obtain:
- A user's list of ingredients
- The list of all recipes
- Scrape new recipes based off a category and a user's ingredients. (To-do:
this takes two to three minutes, and needs polishing.)

Can use at: cookmate-api-production.up.railway.app

## Usage
- Install Python requirements: ``` pip install -r requirements.txt```
- Start the server for development: ``` python main.py ```

### End points
- ```/list``` [GET] Given a recipeID, returns recipe information, if no
parameters are given, returns all recipes in firestore.
- ```/recipes``` [GET] Given a userID and a category, returns recipes
that have those ingredients.
- ```/ingreds``` [GET] Given a userID, returns user's ingredients in firestore.
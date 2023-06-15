<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->

<h3 align="center">Cookmate API</h3>

  <p align="center">
    API created for Cookmate Recipe App that integrates Firestore, Flask and a Web Scraper.
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
This API was created to function as the main backend function for a recipe recollection app [(can find here)](https://github.com/valeria-gonzalez/recipeApp), it's main purpose is to execute a webscraper when the endpoint "/recipe" is called, which extracts the content of recipes from a [website](https://www.bowlofdelicious.com/) and returns a list of those that coincide with a user's ingredients that are obtained from firestore. 

### Built With

[![Python][Python]][Python-url] [![Flask][Flask]][Flask-url] [![Firestore][Firestore]][Firestore-url] 

### Features
- Retrieve and list the ingredients a user has stored in a Firestore collection. This feature allows to filter recipes that coincide with those ingredients.
- Perform web scraping to collect recipes from various sources, based off a category and user ingredients.
- Extract detailed content from specific recipe links, such as title, category, ingredients and instructions.
- Scrape web pages to identify and retrieve links to various recipes. This functionality assists users in discovering new recipes from specific sources or websites.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
__Can try out at: [cookmate-api-production.up.railway.app](cookmate-api-production.up.railway.app)__ <br>
1. Feel free to clone this repository with: ```git clone https://github.com/valeria-gonzalez/cookmateAPI```
2. Install Python requirements: ``` pip install -r requirements.txt```
3. Start the server for development: ``` python main.py ```

```
/list     [GET]    Given a recipeID, returns recipe information, if no parameters are given, returns all recipes in firestore.
/recipes  [GET]    Given a userID and a category, returns recipes that have those ingredients.
/ingreds  [GET]    Given a userID, returns user's ingredients in firestore.
/links    [GET]    Given a category, return a list of links of recipes of a certain category from a website.
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [bowlofdelicious.com](https://www.bowlofdelicious.com/)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/valeria-gonzalez/cookmateAPI.svg?style=for-the-badge
[contributors-url]: https://github.com/valeria-gonzalez/cookmateAPI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/valeria-gonzalez/cookmateAPI.svg?style=for-the-badge
[forks-url]: https://github.com/valeria-gonzalez/cookmateAPI/network/members
[stars-shield]: https://img.shields.io/github/stars/valeria-gonzalez/cookmateAPI.svg?style=for-the-badge
[stars-url]: https://github.com/valeria-gonzalez/cookmateAPI/stargazers
[issues-shield]: https://img.shields.io/github/issues/valeria-gonzalez/cookmateAPI.svg?style=for-the-badge
[issues-url]: https://github.com/valeria-gonzalez/cookmateAPI/issues
[license-shield]: https://img.shields.io/github/license/valeria-gonzalez/cookmateAPI.svg?style=for-the-badge
[license-url]: https://github.com/valeria-gonzalez/cookmateAPI/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/valeria-gonzalez-segura
[Python]: https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
[Firestore]: https://img.shields.io/badge/Firestore-blue?style=for-the-badge&logo=firebase&logoColor=yellow
[Firestore-url]: https://firebase.google.com/docs/firestore

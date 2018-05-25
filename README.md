# A Movie Trailer website.

This movie trailer website receives movie data via an API and displays the movie traier information in a browser.
Its key features include:

- Getting the movie information via an API
- Dynamically generating the movie instances using python classes
- Displaying the move information in a HTML file via a webbrowser


# Usage

To use the application do the following:

- Import the porject file from github via the follwing link (link)
- cd into the porject directory (directory/name)
- run the following file to start the program (starter_file.py)
- Instead of hardcoding my TMDB_API_KEY, I have set it in an env.py file.
- You need to create this file in the root of the repository and then add 
- the following lines to the code:


```sh
import os

os.environ['TMDB_API_KEY'] = 'insert_your_tmdb_api_key_here'
```

- Then run the follwoing in the command line to generate the html file:

```sh
$ python entertainment_center.py
```
### Todos

- Improve the look and feel of the application through bootstrap


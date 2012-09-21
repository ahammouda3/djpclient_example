
Setting up the '3rd party' submodule for git:

After setting up this repo with a simple local clone,

(venv)$ git submodule add -f https://github.com/ahammouda3/djpclient.git djpclient_example/djpclient

(venv)$ cd djpclient_example/djpclient

We want the latest branch I'm using so, I do the following

(venv)$ git checkout -b ga-branch remotes/origin/ga-branch

(venv)$ touch __init__.py # So that this package can be imported by our project settings file

(venv)$ cd ../../

(venv)$ pip install djpclient_example/djpclient

Then of course the app should be added to settings.py (I've added it in both the 
installed apps and with the rest of the middleware classes
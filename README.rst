
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

If you want your submodule to work with a heroku deployment, you'll
need to do the following as well

(venv)$ echo "-e ./djpclient_example/djpclient" >> requirements.txt

The -e here is to ensure that submodule changes are updated at runtime

N.B: I have been unable to find a way to do this submodule deployment 
     successfully where the submodule I want to be updating in deployed 
     mode is a branch.  You must be only asking for changes on the 
     master branch from your 3rd party lib, and you must have those latest
     changes pit to github (depending on how your setup file is written
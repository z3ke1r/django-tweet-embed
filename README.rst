Django Tweet Embed
======================================

Takes a tweet url, requests the ``json`` from Twitter oEmbed, parses the ``json`` for the ``html`` element and returns it to your template. The html returned is ready to go and will be shown as a tweet on your web page. This uses the Requests_ library for Python.


Python Requirements
-------------

::

    $ pip install requests

Installation
-------------
This template tag is ultralite :muscle: so you dont even need to bother installing it as an app. Just create a ``templatetags`` directory within your app directory at the same level as your ``models.py`` file. Then create the ``__init__.py`` and ``tweet_tags.py`` files. All of this can be copied from the repo  :wink:.

::

    appfolder/
        __init__.py
        models.py
        views.py
        templatetags/ #create this if you dont have one already.
            __init__.py #create this! It's just an empty file but all template tags require it!!
            tweet_tags.py #you get the idea...it's in the repo.

DjangoDocs_  
As with any new template tag you should restart the server to ensure the tag is registered.

Usage
-----
To use the tag in your template include the ``{% load tweet_tags %}`` in your template and you are good to go! Just use the tag and give it a url.
::

  {% tweet_tags <tweeturl> %}
  

``<tweeturl>`` is the url to the tweet you want embedded on your page. It can be hard coded or a variable passed from your view.

``{% autoescape off %}`` ``{% endautoescape %}`` tags can be wrapped around the ``{% tweet_tags <tweeturl> %}`` to stop the html from being escaped by the django interpreter. This is neccesary unless you already have the django environment variable turned off.


Example: 

This will loop through the "tweets" queryset defined in the view. Send the url of each tweet object to the tag function and return the embed html into the ``mdl-card`` div in the template.

``template.html``
::

  {% load tweet_tags %}
  
  
  {% for x in tweets %}
      <div class="mdl-card__media">
          {% autoescape off %}{% tweet_tags x.url %}{% endautoescape %}
          <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
      </div>
  {% endfor %}

``views.py``
::

  def template(request):
    if request.user.is_authenticated:
        tweets = tweet.objects.filter(user=request.user)
        return render(request, 'app/template.html', {'tweets': tweets})
    else:
        return redirect('login')


.. _Requests: https://pypi.org/project/requests/
.. _DjangoDocs: https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/#code-layout

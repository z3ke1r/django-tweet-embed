Django Tweet Embed
======================================

Provides templatetags for:
* 'Embedding a tweet'

Takes a tweet url, requests the ``json`` from Twitter oEmbed, parses the ``json`` for the ``html`` element and returns it to your template. The html returned is ready to go and will be shown as a tweet on your web page.


Requirements
-------------

::

    $ pip install requests


Usage
-----
::

  {% tweet_tags <tweeturl> %}
  

``<tweeturl>`` may contain any tweets url.

``{% autoescape off %}`` ``{% endautoescape %}`` tags can be wrapped around the ``{% tweet_tags <tweeturl> %}`` to stop the html from being escaped by the django interpreter.


Example ``template.html``::

  {% load tweet_tags %}
  
  
  {% for x in tweets %}
      <div class="mdl-card__media">
          {% autoescape off %}{% tweet_tags x.url %}{% endautoescape %}
          <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
      </div>


Templates
---------

Templates are in:

* ``django/templatetags/``


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.views import generic

URL_RELEVANTS = "http://198.199.65.250:8001/most_relevants"
URL_MENTIONS = "http://198.199.65.250:8001/most_mentions"
ID_LOCAWEB = 42


def get_most(name):
    # get relevants in api
    result = None
    if name == "relevants":
        url = URL_RELEVANTS
    elif name == "mentions":
        url = URL_MENTIONS
    try:
        url = url + "/" + str(ID_LOCAWEB)
        r = requests.get(url)
        result = r.json()
    except Exception, e:
        print e

    return result


class MostRelevants(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MostRelevants, self).get_context_data(**kwargs)
        context["results"] = get_most("relevants")
        return context


class MostMentions(generic.TemplateView):
    template_name = "most_mentions.html"

    def get_context_data(self, **kwargs):
        context = super(MostMentions, self).get_context_data(**kwargs)
        context["results"] = get_most("mentions")
        list_group = []
        tweets = []

        if context["results"]:
            for group in context["results"].itervalues():
                for user in group:
                    text = user.get('text')
                    likes = user.get('likes')
                    link_tweet = user.get('link_tweet')
                    retweets = user.get('retweets')
                    date = user.get('date')

                    name = user.get('user').get('screen_name')

                    tweets.append({
                        "text": text,
                        "likes": likes,
                        "link_tweet": link_tweet,
                        "retweets": retweets,
                        "date": date
                    })
                list_group.append({
                    "name": name,
                    "tweets": tweets
                })
                tweets = []
        context["results"] = list_group

        return context

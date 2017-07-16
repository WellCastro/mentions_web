# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic


class Index(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["results"] = ""

        return context
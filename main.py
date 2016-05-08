#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import jinja2
import webapp2

from datetime import datetime

import dna

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("root.html")

    def post(self):
        vpisani_dnk = self.request.get("dna")
        tekst = "Vhodni DNK: {}".format(vpisani_dnk)
        izhodni_podatki = {
            "dnk" : dna,
            "lasje" : dna.get_hair_color(vpisani_dnk),
            "oblika_obraza" : dna.get_face_shape(vpisani_dnk),
            "barva_oci"  :  dna.get_eyes_colour(vpisani_dnk),
            "spol"  : dna.get_sex(vpisani_dnk),
            "rasa" : dna.get_race(vpisani_dnk),
            "osumljenec" : dna.get_person(vpisani_dnk)
        }
        self.render_template("analiza.html", params=izhodni_podatki)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler)
], debug=True)

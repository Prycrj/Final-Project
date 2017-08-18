#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
import jinja2
import os
#import requests
import json
from pprint import pprint
from google.appengine.api import urlfetch
import urllib2
import urllib
import logging



env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('index.html')
        template_values = {'a': 1}
        self.response.write(template.render(template_values))
    def post(self):
        input_field = self.request.get('user_query')

        lat = self.request.get('lat')
        lng = self.request.get('lng')

        logging.info(self.request.POST)
        template = env.get_template('result.html')
        self.response.write(template.render( {'lat': lat, 'lng':lng} ))





class mapHandler(webapp2.RequestHandler):
    def get(self):
        count_template = JINJA_ENVIRONMENT.get_template("result.html")
        self.response.write(count_template.render())

#class signin(webapp2.RequestHandler):
    #def get(self):
        #count_template = JINJA_ENVIRONMENT.get_template("store.html")
        #self.response.write(count_template.render())


app = webapp2.WSGIApplication([
    #('/', signin),
    ('/',MainHandler),
    ('/map', mapHandler)


], debug=True)

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



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        count_template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(count_template.render())

    def post(self):
        googleAPI_template = JINJA_ENVIRONMENT.get_template("result.html")
        user_query = self.request.get("user_query")
        base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

        url_params = {'location': "40.6665,-73.9576" ,'radius':"500",'types':'food','name': user_query, 'key': 'AIzaSyAO1qeFArYbQ16zHyYe0Bojfj6rLhzNv6U'}
        googlemap_data = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()
        json_data = json.loads(googlemap_data)
        logging.info(json_data['results'][0]['geometry']['location'])
        #self.response.write(json_data)
        result_dict = json_data['results'][0]['geometry']['location']
        self.response.write(googleAPI_template.render(result_dict))



        #for item in json_data['data']:
        #    self.response.write('<h2>' + item['']['original'] + '<br/><br/></h2>' )



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

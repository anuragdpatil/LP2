import os
import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_views = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_views))
        
    def post(self):
        longitude = self.request.get('longitude')
        latitude = self.request.get('latitude')
        
        url = "https://api.open-meteo.com/v1/forecast?" + "latitude="+latitude+"&longitude="+longitude+"&hourly=temperature_2m"
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        
        template_views = data
        path = os.path.join(os.path.dirname(__file__), 'success.html')
        self.response.out.write(template.render(path, template_views))
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


#cloud terminal command : py google-cloud-sdk/bin/dev_appserver.py C:\Users\sahil\CCL_trial\1_to_3\app.yaml
import webapp2
import urllib
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>'
        '<form action="/result" method="post">'
        '<label>Zipcode</label><b>'
        '<input type="text" name="zipcode" placeholder="111111" pattern=[0-9]{6} required><br>'
        '<input type="submit" name="submit"><br>'
        '</form></body></html>'
        )

class Result(webapp2.RequestHandler):
    def post(self):
        zipcode = self.request.get('zipcode')

        if len(zipcode)!=6 and not zipcode.isdigit():
            self.response.write('<html><body>'
            '<h1>Error</h1>'
            '<a href="/">Go back</a>'
            )
        
        url = 'http://api.postalpincode.in/pincode/' + str(zipcode)
        response = urllib.urlopen(url).read()
        response = json.loads(response)

        if response[0]['Status']=="Error":
            self.response.write('<html><body>'
            '<h1>Error</h1>'
            '<a href="/">Go back</a>'
            )
        else:
            self.response.write("Nearest Post Offices: <br>")
            self.response.write("Zipcode: "+str(zipcode)+"<br>")

            for i in response[0]['PostOffice']:
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("Pincode: "+str(i["Pincode"])+"<br>")
                self.response.write("--------------------------<br><br>")

app = webapp2.WSGIApplication([('/', MainPage), ('/result', Result)], debug=True)

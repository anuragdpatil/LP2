import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range (5):
            self.response.out.write("Anurag Patil </br>")
            self.response.out.write("T190058659 </br>")
            self.response.out.write("IT </br>")
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
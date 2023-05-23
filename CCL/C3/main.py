import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        i=0
        while i<10:
            self.response.out.write("Anurag Patil </br>")
            self.response.out.write("T190058659 </br>")
            i+=1
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
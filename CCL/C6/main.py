import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        def fib(n):
            if n<=1:
                return n
            return fib(n-2)+fib(n-1)
        for i in range (8):
            self.response.out.write(fib(8))
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
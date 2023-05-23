import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<table border="1" cellspacing="2">')
        for i in range (1,11):
            self.response.write('<tr>')
            self.response.write('<td>10 x'+str(i)+'</td>'+'<td>=</td>'+'<td>'+str(10*i)+'</td>')
            self.response.write('</tr>')
            self.response.write('</table')
            
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
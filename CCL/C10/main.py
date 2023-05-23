import webapp2
import urllib
import json
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('<html><body>'
		'<form action="/result" method="POST">'
		'<label>University Name<label>'
		'<input type="text" name="universityName" required>'
		'<input type="submit" name="submit">'
		'</form></body></html>'
		)


class Result(webapp2.RequestHandler):
	def post(self):
		universityName = self.request.get("universityName")
		universityName=universityName.split()
		universityName='+'.join(universityName)
		url="http://universities.hipolabs.com/search?name="+universityName
		data=urllib.urlopen(url).read()
		data=json.loads(data)
		
		self.response.write('<h2>Matched Universities</h2>')
		self.response.write('<hr>')
		for single_data in data:
			self.response.write("Name"+single_data['name'].encode('utf-8')+"<br>")
			self.response.write('Country:'+str(single_data['country'])+"<br>")
			self.response.write('Alpha Two Code:'+str(single_data['alpha_two_code'])+"<br>")
			self.response.write('Alpha Three Code:'+str(single_data['alpha_three_code'])+"<br>")
			self.response.write('Latitude:'+str(single_data['latitude'])+"<br>")
			self.response.write('Web Pages:<ul>')
			for web_page in single_data['web_pages']:
				self.response.write('<li>'+web_page+'</li>')
			self.response.write('</ul>')
			#if len(single_data["domains"])!=0:
			self.response.write("Domains:<ul>")
			for domain in single_data['domains']:
				self.response.write("<li>"+str(domain)+"</li>")
			self.response.write('</ul>')
			
			if single_data['state-province']!=None:
				self.response.write("State-Province:"+single_data['state-province'].encode('utf-8')+"<br>")
			self.response.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>")
			
			
			
					
			
		#self.response.write(str(data))
		
			
app = webapp2.WSGIApplication([("/",MainPage),("/result",Result)], debug=True)

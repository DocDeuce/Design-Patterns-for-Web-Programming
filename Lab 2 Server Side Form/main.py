'''
Justin Henry
8/10/2014
DPW - Online
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler): #Declaring a class
    def get(self): #The function to start everything
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

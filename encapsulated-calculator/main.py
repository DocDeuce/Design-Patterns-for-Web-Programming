'''
Justin Henry
8/13/2014
DPW - Online
Encapsulated Calculator
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass
        #Mal

        #Zoe

        #Wash

        #Kaylee

        #Jayne

class Earnings(object):
    def __init__(self):
        pass

    @property
    def contribution(self):
        pass

    @contribution.setter
    def contribution(self, adjustment):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

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
        m = Earnings()
        m.mon =
        m.tue =
        m.wed =
        m.thu =
        m.fri =

        #Zoe
        z = Earnings()
        z.mon =
        z.tue =
        z.wed =
        z.thu =
        z.fri =

        #Wash
        w = Earnings()
        w.mon =
        w.tue =
        w.wed =
        w.thu =
        w.fri =

        #Kaylee
        k = Earnings()
        k.mon =
        k.tue =
        k.wed =
        k.thu =
        k.fri =

        #Jayne
        j = Earnings()
        j.mon =
        j.tue =
        j.wed =
        j.thu =
        j.fri =

class Earnings(object):
    def __init__(self):
        self.mon = 0
        self.tue = 0
        self.wed = 0
        self.thu = 0
        self.fri = 0
        self.total = 0
        self.__contribution = 0

    @property
    def total(self):
        self.total = self.mon + self.tue + self.wed + self.thu + self.fri
        return self.total

    @property
    def contribution(self):
        self.__contribution = self.total/(m.total + z.total + w.total + k.total + j.total)
        return self.__contribution

    @contribution.setter
    def contribution(self, adjustment):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

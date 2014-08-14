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
        m.mon = 150
        m.tue = 320
        m.wed = 85
        m.thu = 202
        m.fri = 237
        m.total = 1154
        self.response.write(str(m.total) + " " + str(m.average))

        #Zoe
        z = Earnings()
        z.mon = 176
        z.tue = 278
        z.wed = 76
        z.thu = 189
        z.fri = 255
        z.calc_total()
        self.response.write(str(z.total) + " " + str(z.average))

        #Wash
        w = Earnings()
        w.mon = 97
        w.tue = 156
        w.wed = 54
        w.thu = 101
        w.fri = 166

        #Kaylee
        k = Earnings()
        k.mon = 92
        k.tue = 123
        k.wed = 48
        k.thu = 88
        k.fri = 115

        #Jayne
        j = Earnings()
        j.mon = 142
        j.tue = 258
        j.wed = 72
        j.thu = 163
        j.fri = 240

class Earnings(object):
    def __init__(self):
        self.mon = 0
        self.tue = 0
        self.wed = 0
        self.thu = 0
        self.fri = 0
        self.__total = 0
        self.__average = 0

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, adjustment):
        self.__total = adjustment

    def calc_total(self):
        self.__total = self.mon + self.tue + self.wed + self.thu + self.fri

    @property
    def average(self):
        self.__average = (self.mon + self.tue + self.wed + self.thu + self.fri)/5
        return self.__average

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

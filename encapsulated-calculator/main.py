'''
Justin Henry
8/13/2014
DPW - Online
Encapsulated Calculator
'''
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        g = Page()

        self.response.write(g.page_head)


        crew = {"Mal":[150,320,85,202,237],
                "Zoe":[176,278,76,189,255],
                "Wash":[97,156,54,101,166],
                "Kaylee":[92,123,48,88,115],
                "Jayne":[142,258,72,163,240]}

        for c in crew:
            g.who = c
            g.comp = crew.get(c, "none")
            g.total_spot = ""
            self.response.write(g.crew_build() + g.calculate())



        if self.request.GET:
            print "working"
            r = self.request.GET
            e = Earnings()
            e.pay = [int(r["mon"]),int(r["tue"]),int(r["wed"]),int(r["thu"]),int(r["fri"])]
            e.calc_total()
            g.total_spot = #e.total

        self.response.write(g.page_close)

class Earnings(object):
    def __init__(self):
        self.pay = 0
        self.__total = 0

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, adjustment):
        self.__total = adjustment

    def calc_total(self):
        self.__total = sum(self.pay)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

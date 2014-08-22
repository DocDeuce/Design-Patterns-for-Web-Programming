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
        g = Page() #Set the Page object as easily accessible
        crew = {"Mal":[150,320,85,202,237],
                "Zoe":[176,278,76,189,255],
                "Wash":[97,156,54,101,166],
                "Kaylee":[92,123,48,88,115],
                "Jayne":[142,258,72,163,240]} #This dictionary contains five crew members of the ship Serenity and their pay for each day of a work week
        if self.request.GET: #If form data has been submitted, run the following
            self.response.write(g.page_head) #This writes the opening html, and body tag, and also contains the page title and the css link
            r = self.request.GET #Set the request as easily accessible
            g.whom = r["who"] #This sets the whom value of the Page object to the value named by the form as "who"
            e = Earnings() #Set the earnings method as easily accessible
            e.pay = [int(r["mon"]),int(r["tue"]),int(r["wed"]),int(r["thu"]),int(r["fri"])] #This creates an array to be sent into the Earnings method
            g.pay = [int(r["mon"]),int(r["tue"]),int(r["wed"]),int(r["thu"]),int(r["fri"])] #This creates the same array to be sent into the Page Object
            e.calc_total() #This requests that the method for calculating the total weekly compensation be called from the Earnings object
            g.total_spot = "Total: " + str(e.total) #Uses the setter in the Page object to display the total calculated by the Earnings object
            self.response.write(g.indi_build() + g.p_begin + str(g.total_spot) + g.p_end + g.div_end + g.page_close) #Writes the individual crew member, ther pay per day, and their total pay for the week
        else: #Without form data being submitted, do the following
            self.response.write(g.page_head) #This writes the opening html, and body tag, and also contains the page title and the css link
            for c in crew: #Begin iterating through the crew dictionary
                g.who = c #Sets the value of "who" in the Page object the key in the index of c in the dictionary
                g.comp = crew.get(c, "none") #This returns an array of all of the number values associated with the crew member at the current index and sets the it as the value of "comp" in the Page object
                self.response.write(g.crew_build() + g.calculate() + g.div_end) #run the method to display crew member information in a div and then close that div
            self.response.write(g.page_close) #Close the html and body tag

class Earnings(object): #This class handles the numbers from the dictionary
    def __init__(self): #Initiate yourself!
        self.pay = 0 #Establishes the variable to have its value set by the MainHandler
        self.__total = 0 #Private total to be calculated upon method call

    @property #A decorator to establish a getter
    def total(self):
        return self.__total #This returns a private total from a public method

    @total.setter #An unused setter, just in case Captain Mal wants to make some pay adjustments
    def total(self, adjustment): #The setter requires two parameters, I called the second one adjustment
        self.__total = adjustment

    def calc_total(self): #Method to be called in order to calculate the total weekly compensation
        self.__total = sum(self.pay) #Deduces the sum of all values in an array and sets it as the private total

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

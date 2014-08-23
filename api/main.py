'''
Justin Henry
8/22/2014
DPW - Online
Proof of Concept
'''
import webapp2
import urllib2 #Necessary to request, receive, and open data
from xml.dom import minidom # Used to parse through received data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage() #Calls the subclass of the superclass "Form"
        p.input = [['text', 'zip', 'Zip Code'], ['submit', 'Submit']] #An array of arrays used to set html input attributes
        self.response.write(p.display()) #displays html page from FormPage class
        if self.request.GET: #If form data has ben submitted, do the following
            zip = self.request.GET['zip'] #sets zip variable value to what is received from input
            url = "http://whoismyrepresentative.com/getall_mems.php?zip=" + zip #For accessing the api information and the variable "zip" to be submitted via html form input
            request = urllib2.Request(url) #Sets variable for urllib2 to request data from the url listed above
            opener = urllib2.build_opener() #Creates object to receive data from url
            result = opener.open(request) #Use the receiving object to open the data requested from the url
            xmldoc = minidom.parse(result) #Parse the result of the request
            self.content = "<br/>" #Initiate the display of the received data
            list = xmldoc.getElementsByTagName('rep') #Creates an array of the primary objects received from the request
            for item in list: #Iterate though the list of results and do the following for each to build and display the information
                self.content += "Name: "+item.attributes["name"].value
                self.content += " Party: "+item.attributes["party"].value
                self.content += " District: "+item.attributes["district"].value
                self.content += " Phone: "+item.attributes["phone"].value
                self.content += " Office "+item.attributes["office"].value
                self.content += " Website: "+item.attributes["link"].value
                self.content += "<br/>"

            self.response.write(self.content) #Display the accumulated content

class Page(object): #A superclass to contain the necessary html for building a page
    def __init__(self):
        self._page_head = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Proof of Concept</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        self._page_body = ""
        self._page_close = '''
    </body>
</html>'''

class FormPage(Page): #A subclass of the Page superclass that creates the html form
    def __init__(self):
        super(FormPage, self).__init__() #The superclass for this subclass is Page, get it going
        self._form_open = '''
        <form method="GET">'''
        self.__input = [] #An empty array to contain
        self._form_inputs = ""
        self._form_close = '''
        </form>'''

    @property #Unused but necessary getter
    def input(self):
        pass

    @input.setter
    def input(self, arr):
        self.__input = arr #Access the private variable
        for item in arr: #Iterate through the array and perform the follwing
            self._form_inputs += '<input type="' + item[0] + '" name="' + item[1] #creates html input and sets attribute values
            try: #Attemt to do the following if the means are available
                self._form_inputs += '" placeholder="' + item[2] +'" />' #Adds placeholder attribute and its value to input and closes it
            except: #if the above cannot be done, do the following
                self._form_inputs += '" />' #Close the input tag

    def display(self): #Method for displaying html page
        return self._page_head + self._page_body + self._form_open + self._form_inputs + self._form_close + self._page_close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

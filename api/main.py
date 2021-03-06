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
        p.input = [['text', 'zip', 'Zip Code'], ['submit', 'submit', 'KNOW']] #An array of arrays used to set html input attributes

        if self.request.GET: #If form data has been submitted, do the following
            rm = RepModel()
            rm.zip = self.request.GET['zip'] #sets zip variable value to what is received from input
            rm.callApi()
            rv = RepView() #Calls the method to create the data display
            rv.rdos = rm.dos #Takes data from Model and gives to View class
            p._page_body = rv.content
            p._footer_text = "<p>Enter another zip code to see the representatives for a different area</p>"
        else:
            p._page_body = '''
        <div class="home">
            <section>
                <p><span class="xxl">KNOW</span> who represents you in the Senate and House of Representatives</p>
            </section>
            <section>
                <p><span class="xxl">REACH</span> your representatives by mail, phone, or email</p>
            </section>
            <section>
                <p><span class="xxl">EFFECT</span> the policies and laws that effect you</p>
            </section>
        </div>
            '''
            p._footer_text = "<p>Enter your zip code to find your senators and representatives</p>"
        self.response.write(p.display()) #displays html page from FormPage class
        #print rv.content

class RepView(object):
    '''Handle the data display'''
    def __init__(self):
        self.__rdos = []
        self.__content = "" #self.sens() + self.reps() #Initiate the display of the received data
        self.__reps = ""
        self.__sens = ""

    def update(self):
        for do in self.__rdos:
            whosit = "<tr><td>" + do.name + "</td><td>" + do.party + "</td><td>" + do.district + "</td><td>" + do.phone + "</td><td>" + do.office + "</td><td>" + do.website + "</td></tr>"
            if len(do.district) < 3:
                self.__reps += whosit
            else:
                self.__sens += whosit
        self.__content += "<div class='show'>" + self.sens() + self.reps() + "</div>"

    def sens(self):
        t = Table()
        t.position = "Senators"
        t.description = "Your senators play a role in deciding new laws and confirming people for political positions. Contact your senators to let them know how you feel about any new proposed laws and potential judges."
        t.ps = self.__sens
        return t.construct()


    def reps(self):
        t = Table()
        t.position = "Representatives"
        t.description = "Your representatives can in itiate bills which may turn into laws They can also impeach people. Contact your representatives to let them know about laws you would like to see in and people you would like to see out."
        t.ps = self.__reps
        return t.construct()
            #Display the accumulated content

    @property
    def content(self):
        return self.__content

    @property
    def rdos(self):
        pass

    @rdos.setter
    def rdos(self, arr):
        self.__rdos = arr
        self.update()

class RepModel(object):
    ''' receiving, sorting, and parsing data '''
    def __init__(self):
        self.__url = "http://whoismyrepresentative.com/getall_mems.php?zip="  #For accessing the api information
        self.__zip = "" #store zip
        self.__xmldoc = ""

    def callApi(self):
        request = urllib2.Request(self.__url + self.__zip) #Sets variable for urllib2 to request data from the url listed above
        opener = urllib2.build_opener() #Creates object to receive data from url
        result = opener.open(request) #Use the receiving object to open the data requested from the url
        self.__xmldoc = minidom.parse(result) #Parse the result of the request
        #Sort the data
        list = self.__xmldoc.getElementsByTagName('rep') #Creates an array of the primary objects received from the request
        self._dos = []
        for rep in list:
            do = RepData()
            do.name = rep.attributes["name"].value
            do.party = rep.attributes["party"].value
            do.district = rep.attributes["district"].value
            do.phone = rep.attributes["phone"].value
            do.office = rep.attributes["office"].value
            do.website = rep.attributes["link"].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z

class RepData(object):
    ''' this data object holds the data received by the model and shown by the view '''
    def __init__(self):
        self.name = ""
        self.party = ""
        self.district = ""
        self.phone = ""
        self.office = ""
        self.website = ""

class Page(object): #A superclass to contain the necessary html for building a page
    def __init__(self):
        self._page_head = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Final Project</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        self._page_body = ""
        self._footer_open = '''
        <footer>'''
        self._footer_text = ""
        self._page_close = '''
        </footer>
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
            if item[0] == 'submit': #Attemt to do the following if the means are available
                self._form_inputs += '" value="' + item[2] +'" />' #Adds placeholder attribute and its value to input and closes it
            else: #if the above cannot be done, do the following
                self._form_inputs += '" placeholder="' + item[2] +'" />' #Close the input tag

    def display(self): #Method for displaying html page
        return self._page_head + self._page_body + self._footer_open + self._footer_text + self._form_open + self._form_inputs + self._form_close + self._page_close

class Table(object):
    def __init__(self):
        #super(Table, self).__init__()
        self._pubserv = '''
        <article>
            <section>
                <h2>{self.position}</h2>
                <p>{self.description}</p>
            </section>
            <section>
                <table>
                    <tr>
                        <th>NAME</th>
                        <th>PARTY</th>
                        <th>DISTRICT</th>
                        <th>PHONE</th>
                        <th>OFFICE</th>
                        <th>WEBSITE</th>
                    </tr>
                    {self.ps}
                </table>
            </section>
        </article>
        '''

    def construct(self):
        servants = self._pubserv
        servants = servants.format(**locals())
        return servants

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

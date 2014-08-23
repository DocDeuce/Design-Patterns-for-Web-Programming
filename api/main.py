'''
Justin Henry
8/22/2014
DPW - Online
Proof of Concept
'''
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.input = [['text', 'zip', 'Zip Code'], ['submit', 'Submit']]
        self.response.write(p.display())
        if self.request.GET:
            zip = self.request.GET['zip']
            url = "http://whoismyrepresentative.com/getall_mems.php?zip=" + zip
            request = urllib2.Request(url)
            opener = urllib2.build_opener()
            result = opener.open(request)
            xmldoc = minidom.parse(result)
            self.content = "<br/>"
            list = xmldoc.getElementsByTagName('rep')
            for item in list:
                self.content += "Name: "+item.attributes["name"].value
                self.content += " Party: "+item.attributes["party"].value
                self.content += " District: "+item.attributes["district"].value
                self.content += " Phone: "+item.attributes["phone"].value
                self.content += " Office "+item.attributes["office"].value
                self.content += " Website: "+item.attributes["link"].value
                self.content += "<br/>"

            self.response.write(self.content)

class Page(object):
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

    def display(self):
        return self._page_head + self._page_body + self._page_close

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '''
        <form method="GET">'''
        self.__input = []
        self._form_inputs = ""
        self._form_close = '''
        </form>'''

    @property
    def input(self):
        pass

    @input.setter
    def input(self, arr):
        self.__input = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[0] + '" name="' + item[1]
            try:
                self._form_inputs += '" placeholder="' + item[2] +'" />'
            except:
                self._form_inputs += '" />'

    def display(self):
        return self._page_head + self._page_body + self._form_open + self._form_inputs + self._form_close + self._page_close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

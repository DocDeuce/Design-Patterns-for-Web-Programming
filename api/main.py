'''
Justin Henry
8/22/2014
DPW - Online
Proof of Concept
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.input = [['text', 'Zip Code', 'zip_code'], ['submit', 'Submit']]
        self.response.write(p.display())

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


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self.title = "MadLib"
        self.head = '''
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        '''
        self.body = "Testing"
        self.close = '''
    </body>
</html>
        '''

    def print_out(self):
        return self.head + self.body + self.close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

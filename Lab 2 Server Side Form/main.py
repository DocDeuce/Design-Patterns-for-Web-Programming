'''
Justin Henry
8/10/2014
DPW - Online
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler): #Declaring a class
    def get(self): #The function to start everything
        page_head = '''<!DOCTYPE html> 
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''

        page_body = '''
        '''

        page_close = '''
    </body>
</html>'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

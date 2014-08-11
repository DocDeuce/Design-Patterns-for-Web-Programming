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
        <form method="GET" action="">
            <label>Name: </label><input type="text" name="user">
            <label>Gender: </label><select name="gender">
                <option>Male</option>
                <option>Female</option>
            </select><br/>
            <label>Email: </label><input type="text" name="email"><br/>
            <label>Destination: </label><input type="text" name="destination"><br/>
            <p>What is the reason for your travel? </p><br/>
            <label>Business</label><input type="checkbox" name="purpose" value="business"><br/>
            <label>Pleasure</label><input type="checkbox" name="purpose" value="pleasure"><br/>
            <input type="submit" value="Submit">
        </form>'''

        page_close = '''
    </body>
</html>'''

        if self.request.GET:
            user = self.request.GET["user"]
            gender = self.request.GET["gender"]
            email = self.request.GET["email"]
            destination = self.request.GET["destination"]
            purpose = self.request.GET["purpose"]
        else:
            self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

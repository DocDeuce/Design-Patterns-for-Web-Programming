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
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        page_body = '''
        <form method="GET" action="">
            <label>Gender: </label><select name="gender" placeholder="select">
                <option selected>Select</option>
                <option>Male</option>
                <option>Female</option>
            </select><br/>
            <label>Name: </label><input type="text" name="user"><br/>

            <label>Email:</label><input type="text" name="email"><br/>
            <label>Destination:</label><input type="text" name="destination"><br/>
            <p>What is the reason for your travel? </p>
            <label class="check">Business</label><input type="checkbox" name="purpose" value="business"><br/>
            <label class="check">Pleasure</label><input type="checkbox" name="purpose" value="pleasure"><br/>
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
            self.response.write("Hello, " + user + "! Check your email address, " + email + ", for confirmation of your " + purpose + " trip to " + destination + ". ")
            if gender == "Male":
                self.response.write("While in " + destination + " you might enjoy some of the sporting events that take place")
            if gender == "Female":
                self.response.write("You might enjoy some of the spas that " + destination + " has to offer.")
        else:
            self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

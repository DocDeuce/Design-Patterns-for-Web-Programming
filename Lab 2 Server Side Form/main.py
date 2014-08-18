'''
Justin Henry
8/10/2014
DPW - Online
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler): #Declaring a class
    def get(self): #The function to start everything
        #page_head constructs html up to the body tag
        page_head = '''<!DOCTYPE html>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        #An html form using the "GET" methos and containing a select, 3 inputs, 2 checkboxes and a submit button
        page_body_form = '''
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

        p_open = '''<p class="result">''' #To allow styling, I wrap the results in this paragraph tag
        p_close = '''</p>''' #Closing paragraph tag

        #Closing the html to prevent errors
        page_close = '''
    </body>
</html>'''

        if self.request.GET:
            user = self.request.GET["user"] #variable to contain name entered by user
            gender = self.request.GET["gender"] #variable to contain gender selected by user with the option selector
            email = self.request.GET["email"] ##variable to contain email address entered by user
            destination = self.request.GET["destination"] #variable to contain destination entered by user
            purpose = self.request.GET["purpose"] #variable to contain purpose selected by user with checkbox
            result = "Hello, " + user + "! Check your email address, " + email + ", for confirmation of your " + purpose + " trip to " + destination + ". " #A variable to contain a string that includes user entered data
            actvt = "" #empty variable that will receive its value based on a condition

            if gender == "Male": #Condition to determine value of actvt
                actvt = "While in " + destination + " you might enjoy some of the sporting events that take place." #Gender specific result
            if gender == "Female": #Condition to determine value of actvt
                actvt = "You might enjoy some of the spas that " + destination + " has to offer." #Gender specific result

            self.response.write(page_head + p_open + result + actvt + p_close + page_close) #this will write the html and rsults to the page, including the gender specific actvt value

        else:
            self.response.write(page_head + page_body_form + page_close) #if no form data is entered, this will display the form

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

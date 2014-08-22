'''
Justin Henry
8/13/2014
DPW - Online
Encapsulated Calculator
'''

class Page(object): #Page object to build html and to be imported into the main handler

    def __init__(self): #Initiate yourself!

        #The head of the html establishing the document type and title, linking the css, and opening the body tag
        self.page_head = '''<!DOCTYPE html>
<html>
    <head>
        <title>Encapsulated Calculator</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''

        #A div to contain and display each crew member's name and earnings for each weekday
        self.crew_show = '''
        <div>
            <h2>{self.who}</h2>
            <p>Mon: {self.comp[0]}</p><br/>
            <p>Tue: {self.comp[1]}</p><br/>
            <p>Wed: {self.comp[2]}</p><br/>
            <p>Thu: {self.comp[3]}</p><br/>
            <p>Fri: {self.comp[4]}</p><br/>
        ''' #A loop was used to iterate though a dictionary of crew members and their compensation, hence the brackets

        #This div displays the individual who's total weekly compensation was requested, it has the same format as crew show but pulls its information from a form
        self.indi_show = '''
        <div>
            <h2>{self.whom}</h2>
            <p>Mon: {self.pay[0]}</p><br/>
            <p>Tue: {self.pay[1]}</p><br/>
            <p>Wed: {self.pay[2]}</p><br/>
            <p>Thu: {self.pay[3]}</p><br/>
            <p>Fri: {self.pay[4]}</p><br/>
        '''
        #This form contains the crew names and pay amounts from the dictionary in order to submit it but hides the inputs to receive hard coded data
        self.page_form = '''
            <form method="GET" action="">
                <input type="hidden" name="who" value="{self.who}">
                <input type="hidden" name="mon" value="{self.comp[0]}">
                <input type="hidden" name="tue" value="{self.comp[1]}">
                <input type="hidden" name="wed" value="{self.comp[2]}">
                <input type="hidden" name="thu" value="{self.comp[3]}">
                <input type="hidden" name="fri" value="{self.comp[4]}">
                <input type="submit" value="Total">
            </form>
        '''
        #an opening paragraph tag to contain the total that will eventually be displayed
        self.p_begin = '''
            <p>'''

        #An empty string whose value will be set upon form submission, displaying total weekly compensation
        self.__total_spot = ""

        #Closing paragraph tag to end the total display
        self.p_end = '''
            </p>'''

        #Closing the div that contains the crew member and their numbers
        self.div_end = '''
        </div>
        '''

        #This closes the html body and the html, ending the page
        self.page_close = '''
    </body>
</html>'''

        #I don't even need this
        self.whole_page = ""

    #This method allows the form on this page to have its values set as the dictionary information from the main file in order to calculate the total compensation
    def calculate(self):
        crew_comp = self.page_form
        crew_comp = crew_comp.format(**locals())
        return crew_comp

    #This method allows the div on this page to have its values set as the dictionary information from the main file in order to display it
    def crew_build(self):
        crew_div = self.crew_show
        crew_div = crew_div.format(**locals())
        return crew_div

    #This method allows the resulting div on this page to have its values set as the information from the main submitted form in order to display it
    def indi_build(self):
        indi_div = self.indi_show
        indi_div = indi_div.format(**locals())
        return indi_div

    #This is a getter of the total that the for calculates, it returns the private information but is called upon as a method
    @property
    def total_spot(self):
        return self.__total_spot

    #This is a setter of the private total that the form calculates
    @total_spot.setter
    def total_spot(self, added):
        self.__total_spot = added



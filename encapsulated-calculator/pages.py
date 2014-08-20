class Page(object):
    def __init__(self):
        self.page_head = '''<!DOCTYPE html>
<html>
    <head>
        <title>Encapsulated Calculator</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.crew_show = '''
        <div>
            <h2>{self.who}</h2>
            <p>Mon: {self.comp[0]}</p><br/>
            <p>Tue: {self.comp[1]}</p><br/>
            <p>Wed: {self.comp[2]}</p><br/>
            <p>Thu: {self.comp[3]}</p><br/>
            <p>Fri: {self.comp[4]}</p><br/>
        '''
        self.indi_show = '''
        <div>
            <h2>{self.whom}</h2>
            <p>Mon: {self.pay[0]}</p><br/>
            <p>Tue: {self.pay[1]}</p><br/>
            <p>Wed: {self.pay[2]}</p><br/>
            <p>Thu: {self.pay[3]}</p><br/>
            <p>Fri: {self.pay[4]}</p><br/>
        '''

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
        self.p_begin = '''
            <p>'''
        self.__total_spot = ""
        self.p_end = '''
            </p>'''
        self.div_end = '''
        </div>
        '''
        self.page_close = '''
    </body>
</html>'''
        self.whole_page = ""

    def calculate(self):
        crew_comp = self.page_form
        crew_comp = crew_comp.format(**locals())
        return crew_comp

    def crew_build(self):
        crew_div = self.crew_show
        crew_div = crew_div.format(**locals())
        return crew_div

    def indi_build(self):
        indi_div = self.indi_show
        indi_div = indi_div.format(**locals())
        return indi_div

    def update(self):
        self.whole_page = self.page_head + self.indi_show + self.p_begin + self.total_spot + self.p_end + self.div_end + self.page_close
        self.whole_page = self.whole_page.format(**locals())

    @property
    def total_spot(self):
        return self.__total_spot

    @total_spot.setter
    def total_spot(self, added):
        self.__total_spot = added
        #self.indi_build()



class Page(object):
    def __init__(self):
        self.page_head = '''<!DOCTYPE html>
<html>
    <head>
        <title>Encapsulated Calculator</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self.crew_show = '''
        <div>
            <h2>{self.who}</h2>
            <p>Mon: {self.comp[0]}</p><br/>
            <p>Tue: {self.comp[1]}</p><br/>
            <p>Wed: {self.comp[2]}</p><br/>
            <p>Thu: {self.comp[3]}</p><br/>
            <p>Fri: {self.comp[4]}</p><br/>
        '''

        self.page_form = '''
            <form method="GET" action="">
                <input type="hidden" name="mon" value="{self.comp[0]}">
                <input type="hidden" name="tue" value="{self.comp[1]}">
                <input type="hidden" name="wed" value="{self.comp[2]}">
                <input type="hidden" name="thu" value="{self.comp[3]}">
                <input type="hidden" name="fri" value="{self.comp[4]}">
                <input type="submit" value="Total">
            </form>
            <div>{self.total_spot}</div>
        </div>'''

        self.page_close = '''
    </body>
</html>'''

    def display(self):
        all = self.page_head + self.page_close
        all = all.format(**locals())
        return all

    def calculate(self):
        crew_comp = self.page_form
        crew_comp = crew_comp.format(**locals())
        return crew_comp


    def crew_build(self):
        '''crew_comp = self.page_form
        crew_comp = crew_comp.format(**locals())'''
        crew_div = self.crew_show
        crew_div = crew_div.format(**locals())
        return crew_div




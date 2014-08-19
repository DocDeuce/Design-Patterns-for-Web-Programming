class Page(object):
    def __init__(self):
        self.page_head = '''<!DOCTYPE html>
<html>
    <head>
        <title>Encapsulated Calculator</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self.page_body = '''
    '''
        self.page_form = '''
        <form method="GET" action="">
            <input type="hidden" name="mon" value="{self.comp[0]}">
            <input type="hidden" name="tue" value="{self.comp[1]}">
            <input type="hidden" name="wed" value="{self.comp[2]}">
            <input type="hidden" name="thu" value="{self.comp[3]}">
            <input type="hidden" name="fri" value="{self.comp[4]}">
            <input type="submit" value="Total">
        </form>'''

        self.page_close = '''
    </body>
</html>'''

    def display(self):
        all = self.page_head + self.page_body + self.page_close
        all = all.format(**locals())
        return all

    def crew_build(self):
        crew_comp = self.page_form
        crew_comp = crew_comp.format(**locals())
        return crew_comp
#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>quem eh voce?</h1>')
else:
    print('<h1>oi <i>%s</i>!</h1>' % cgi.escape(form['user'].value))

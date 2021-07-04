#!/usr/bin/python3.9
import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Pagina de resposta</title>')

if not 'user' in form:
    print('<hr>')
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    print('<hr>')
    print('<h1>quem eh voce?</h1>')
else:
    print('<hr>')
    print('<h1>oi <i>%s</i>!</h1>' % cgi.escape(form['user'].value))

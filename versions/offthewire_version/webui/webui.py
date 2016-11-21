import flask
import gnupg
#https://gist.github.com/dustismo/6203329 / apt-get install libleveldb1 libleveldb-dev && pip install plyvel
#import plyvel #leveldb, very fast, you can even run the database in ram if you want
#import MySQLdb #if you want mysql
from os import urandom
from base64 import b64decode
import datetime


#webui for layerprox 

lp = flask.Flask(__name__) 

dbplace = '' #database directory, test: '/tmp/testdb/'

#general trolling bots
@lp.before_request
def blockuseragentreq():
    useragent = flask.request.headers['User-Agent']
    if 'sqlmap' in useragent:
        return flask.redirect(flask.url_for('dummy'))
    elif 'wget' in useragent:
        return flask.redirect(flask.url_for('dummy'))
    elif 'w3af' in useragent:
        return flask.redirect(flask.url_for('dummy'))
    elif 'curl' in useragent:
        return flask.redirect(flask.url_for('dummy'))
    elif 'Scanner' in useragent:
        return flask.redirect(flask.url_for('dummy'))
        
    else:
        pass



@lp.route('/')
def firstpage():
    return '''

<html>
<head>
<title>LayerProx</title>
</head>
<body>
<h2>
<center>This is a LayerProx server
</h2>
<br>
<br>

<t>get encrypted by goin to /getproxied</t>

</center>
</body>

    </html>
    
    '''


#@lp.route('', methods=['GET'])


@lp.route('/getproxied', methods=['GET', 'POST'])
def get_registerd():
    if flask.request.method == 'POST':
        day = gen_day()
        h1 = urandom()
        fingerprint = 'x'
        return '''
<html>      
<head>

<title> LayerProx</title>
   
   </head>

        <body>
        
        
        </body>


      </html>  
        '''    

    return ''




#make the bots read 1984
@lp.route('/nobots')
def dummy():
    return flask.redirect('http://msxnet.org/orwell/1984.pdf', code=302)

#tell noone pub info, only dax
@lp.route('/robots.txt')
def robots():
    return '''
    User-agent: *
    Dissallow: /
    
    User-agent: DuckDuckBot/1.1
    Dissallow:
    User-agent: DuckDuckBot/1.0
    Dissallow:
    '''

def check_db():
    db = plyvel.DB(dbplace, create_if_missing=True)
    #db.put(b'20', b'value')
    today = datetime.date.today()
    today = str(today)
    #key prefix is date + hmac, one value is date
    for key, value in db.iterator(start=today):
        if key:
            db.delete(key)
        else:
            pass



#datetime syntax
#>>> today = datetime.date.today()
#>>> print today
#2016-11-02
#>>> today = datetime.date.today()
#>>> EndDate = today + timedelta(days=10)
#>>> print EndDate
#2016-11-12


#day generation system
def gen_day():
    test = map(ord, urandom(10))
    test = str(test[0])# first number pair
    test = test[0] # first number
    test = int(test[0])
    test2 = map(ord, urandom(test))

    number = test2[test] 
    today = datetime.date.today()
    number = int(number)
    #number * daytime
    day = today + datetime.timedelta(days=+number) #plus int generated 
    return day


#mysql - db 
#create database lp;
#create table layerprox(
#fingerprint hmac h1 h2 to_date 
#)



if __name__ == '__main__':
    lp.run(debug=False,port=80) #host=0.0.0.0 

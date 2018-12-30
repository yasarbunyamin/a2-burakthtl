#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import request, route, run, debug, default_app

username = "---"
password = "---"

isfood = False
istoys = False
istag = False
isClothes = False
issand = False
choices = []

British_counter = 0
Maine_counter = 0
Scotish_counter = 0
Sphynx_counter = 0


owners_of_MALE = [
    {'name': 'Hasan',
     'model': 1999,
     'birthplace': 'New York',
     'email': 'hasan16@itü.edu.tr'},

    {'name': 'Ali',
     'model': 2000,
     'birthplace': 'Kastamonu',
     'email': 'aali@itü.edu.tr'},

    {'name': 'Necmi',
     'model': 2002,
     'birthplace': 'Adana',
     'email': 'ppre@ytü.edu.tr'},

    {'name': 'Ekin',
     'model': 1999,
     'birthplace': 'Adana',
     'email': 'ekin@ytü.edu.tr'}

]

owners_of_FEMALE = [
    {'name': 'Emre UYSAL',
     'model': 2009,
     'birthplace': 'New York',
     'email': 'uysalem16@itü.edu.tr'},

    {'name': 'Nisa YILDIRIM',
     'model': 2009,
     'birthplace': 'Kastamonu',
     'email': 'anısa@itü.edu.tr'},

    {'name': 'Ensar ESEN',
     'model': 2005,
     'birthplace': 'Adana',
     'email': 'ensaresen@ytü.edu.tr'},

    {'name': 'Eyüb ESEN',
     'model': 1999,
     'birthplace': 'Adana',
     'email': 'eyubesen@ytü.edu.tr'}

]

users = [
    {'username': 'canselizm',
     'password': ''},

    {'username': 'burak',
     'password': 'a'}
]


def html(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />
                  </head>
                  <style style="text/css">
                    body {  background-image: url("https://wallpapercave.com/wp/AbxIDXt.jpg");
                            background-position: 90% 25%;
                             background-repeat:no-repeat;
                             color:white;
                        }
                    a {
                        color:white;}
                  </style>
                  <body>
                      """
    if (title == "Hello" or title == "Sign Up") and username == "---":
        page += content
    elif title != "Hello" and username == "---":
        page += 'You have to log in <br /> <a href="/">Homepage</a>'
    elif title != "Hello" and username != "---":
        page += content
    else:
        page += content
    page += """
          </body>
          </html>"""
    return page


def index():
    welcome = "Hello stranger, welcome to my site!..."
    welcome += '''
        <form action="/login/" method="POST">
            Username: <input name="username" type="text" />
            </br>
            Password: <input name="password" type="password" />
            </br>
            <input value = "Login" type = "submit" />
        </form>
        <a href = /signup/>Sign Up</a>
    '''
    return html("Hello", welcome)


def login():
    global username
    global password
    global users

    post_request = request.POST

    username = str(post_request['username'])
    password = str(post_request['password'])

    iscorrect = False

    for temp in users:
        if temp['username'] == username and temp['password'] == password:
            iscorrect = True
            break
        else:
            iscorrect = False

    if iscorrect:
        return my_website()
    else:
        return login_failed()


def login_failed():
    content = "You are not an allowed user <br />"
    content += '<a href="/">Homepage</ a>'
    return html('Error', content)


def signup():
    title = 'Sign Up'

    content = '''<form method="POST" action="/signup_complete">\n
                 Userame: <input type="text" name="username" /><br />\n
                Password: <input type="password" name="password" /><br />\n
                 <input type="submit" value="Send" />\n
                </form>\n
            '''
    return html(title, content)


def signup_complete():
    global username
    global password
    global users
    post_request = request.POST
    username = str(post_request['username'])
    password = str(post_request['password'])

    users += [{'username': username, 'password': password}]

    return index();


#####################################################333

def S2000_MALE():
    global model
    model = "MALE"
    content = '''<h1 align="center">MALE</h1><p >Typical un-neutered male cat behavior can include some unpleasant habits like urine spraying and responding to females in heat. However, not all cats exhibit these behaviors, and neutering can reduce or eliminate many of them.
                             <fieldset>
                             <legend >IF YOU ARE AN MALE OWNER JOIN MALE CLUB:</legend>
                             ''' + header() + '''

                             </fieldset>
                             '''
    return html('MALE', content)


def S2000_FEMALE():
    global model
    model = "FEMALE"
    content = '''<h1 align="center" >FEMALE</h1><p> Just like with their male counterparts, many of the personality traits in a female cat will depend greatly on whether or not you choose to spay them.</p>
                             <fieldset >
                             <legend>IF YOU ARE AN FEMALE OWNER JOIN FEMALE CLUB:</legend>
                              ''' + header() + '''
                             </fieldset>
      '''

    return html('FEMALE', content)


def header():
    content = '''<nav>\n
                <ul>\n
                <li><a href="/list">List  Owners</a></li>\n
                <li><a href="/add">Join Us</a></li>\n
                <a href="/homepage/">Homepage</a> \n
                </ul>\n
                </nav>\n
            '''
    return content


def S2000_PARTS():
    global issand
    global isClothes
    global istag
    global istoys
    global isfood
    global choices
    content = '''
    <form action="/upgrading">
        <input type="checkbox" name="filter" value ="food">foods</input>
        <input type="checkbox" name="filter" value ="toys">Toys</input>
        <input type="checkbox" name="filter" value ="tag">tag</input>
        <input type="checkbox" name="filter" value ="Clothes">Clothes</input>
        <input type="checkbox" name="filter" value ="sand">sand</input>
        <input type="submit" value="Filter">
    </form>
    '''
    choices = request.query.getall('filter')
    print(choices)
    for temp in choices:
        if str(temp) == "food":
            isfood = True
        if str(temp) == "toys":
            istoys = True
        if str(temp) == "tag":
            istag = True
        if str(temp) == "Clothes":
            isClothes = True
        if str(temp) == "sand":
            issand = True

    content += """<h1 align="center" >WELCOME TO SHOP</h1>"""
    if isfood:
        content += '''
                <table align="center" width="258" border="0"><tr><th width="94" scope="col">foodS</th> <th width="12" scope="col">&nbsp;</th>
                <th width="62" scope="col">COST</th><th width="62" scope="col"> BUY</th></tr><tr><th scope="row">V1</th>
                <td><img src="https://i5.walmartimages.ca/images/Large/703/295/999999-58496703295.jpg" width="100" height="100" alt="V1"></td>
                <td> <div align="center">24$</div></td><td><form method="link" action="https://www.walmart.ca/en/ip/whiskas-meaty-selections-with-real-chicken-dry-cat-food/6000068462987"><input type="submit" value="BUY"></form></td></tr>
                <tr><th scope="row">V2</th><td><img src="https://img.chewy.com/is/image/catalog/64254_MAIN._AC_SL1500_V1508787726_.jpg" width="100" height="100" alt="V2"></td>
                <td><div align="center">34$</div></td><td><form method="link" action="https://www.chewy.com/merrick-purrfect-bistro-grain-free/dp/49214"><input type="submit" value="BUY"></form></td></tr><tr><th scope="row">V3</th>
                <td><img src="https://img.chewy.com/is/catalog/99967_MAIN._AC_SL1500_V1462999359_.jpg" width="100" height="100" alt="V3"></td>
                <td><div align="center">16$</div></td><td><form method="link" action="https://www.chewy.com/meow-mix-original-choice-dry-cat-food/dp/127504"><input name="submit" type="submit" value="BUY"></form></td> </tr>
                </table>
                '''
    content += '<table width="258"  align="center" border="0" >'
    if istoys:
        content += '''
            <tr>
            <th scope="col">&nbsp;</th>
            <th scope="col">&nbsp;</th>
            </tr>
            <tr>
            <th scope="col">Toys</th>
            <th scope="col"><img src="https://images-na.ssl-images-amazon.com/images/I/51-EG8QtZLL._SX425_.jpg" width="100" height="100" alt="Toys"></th>
            <th scope="col">12$</th>
            <th scope="col"><form method="link" action="https://www.amazon.com/HEXBUG-Mouse-Robotic-Cat-Grey/dp/B00SQXVF7A"><input type="submit" value="BUY"></form></td></tr></th>
            </tr>
        '''
    if istag:
        content += '''
            <tr>
            <th scope="row">tag</th>
            <td><img src="https://ae01.alicdn.com/kf/HTB1ST7ZhNOMSKJjSZFlq6xqQFXaW/YVYOO-Pet-Cat-Dog-collar-accessories-Decoration-Pet-ID-Dog-Tags-Collars-stainless-steel-Cat-tag.jpg_640x640.jpg" height="100" alt="tag"></td>
            <td>2$</td>
            <td><form method="link" action="https://www.aliexpress.com/item/YVYOO-Pet-Cat-Dog-collar-accessories-Decoration-Pet-ID-Dog-Tags-Collars-stainless-steel-Cat-tag/32834024671.html"><input type="submit" value="BUY"></form></td></tr></td>
            </tr>
        '''
    if isClothes:
        content += '''
            <tr>
            <th scope="row">Clothes</th>
            <td><img src="https://ae01.alicdn.com/kf/HTB1ATsuXcnrK1RkHFrdq6xCoFXau/15-stil-Pet-Kedi-Kost-m-K-k-K-pek-Kedi-Giyim-Sevimli-Yavru-Kedi-Yavru.jpg_640x640.jpg" width="100" height="100" alt="Clothes"></form></td>
            <td>1$</td>
            <td><form method="link" action="https://tr.aliexpress.com/item/15-stil-Pet-Kedi-Kost-m-K-k-K-pek-Kedi-Giyim-Sevimli-Yavru-Kedi-Yavru/32940236270.html?albbt=Google_7_shopping&isdl=y&slnk=&albslr=234381567&src=google&acnt=494-037-6276&aff_platform=google&crea=tr32940236270&netw=u&plac=&albcp=1626564367&mtctp=&aff_short_key=UneMJZVf&gclid=CjwKCAiA9qHhBRB2EiwA7poaeNl03kDaN37FJHwsRPAlJ-Ru0ORaPKx42e96c27kFZblzPFHUlweGxoCk3AQAvD_BwE&albag=64738897867&albch=shopping&trgt=296904914040&device=c&gclsrc=aw.ds"><input type="submit" value="BUY"></form></td></tr></td>
            </tr>
        '''
    if issand:
        content += '''
            <tr>
            <th scope="row">sand</th>
            <td><img src="data:image/webp;base64,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" width="100" height="100" alt="sand"></td>
            <td>17$</td>
            <td><form method="link" action="https://www.amazon.com/Dr-Elseys-Premium-Clumping-Litter/dp/B0009X29WK?ref_=fsclp_pl_dp_1">
            <input type="submit" value="BUY"></form> </td></tr></td>
            </tr>
        '''
    content += '</table>'

    isfood = False
    istoys = False
    istag = False
    isClothes = False
    issand = False
    return html('SHOP', content)


def my_website():
    content = """
                   <h1  style="text-align:center;">CATS</h1>
                    <p style="clear:both;">Cats have been domesticated for around 4,000 years. While they were once valued for their hunting abilities, they are now valued for their companionship and loving behaviour.<br>
                    While not well known, the collective nouns used for cats and kittens are a clowder of cats and a kindle of kittens.<br>
                    Our domestic cats are known as little cats. They differ from large cats such as lions and tigers because they are naturally active at night and can purr.<br>
                    Cats are now the most popular pet in the UK and in the US.<br>

                    <h3>Which gender do u want?</h3>
                    <form method ="POST" action="/selection_of_model/">
                      <input type="radio" name="model" value="MALE"> MALE<br />
                      <input type="radio" name="model" value="FEMALE"> FEMALE<br />
                      <input value = "Select" type = "submit" />
                    </form>
                    <h1  align="right" style=" float:right:"><a href="/upgrading">SHOP FOR YOUR CAT</a></h1>
                    <h1  align="right" style=" float:right:"><a href="/survey">Survey</a></h1>
                """

    return html('CATS', content)


############################################################################################################################
############################################################################################################################
############################################################################################################################

def survey():
    content = '''
                <h1>What is your favorite cat type?</h1>
                 <form method ="POST" action="/results">
                <table width="258"  align="center" border="0">
                    <tr>
                    <td>British</td>
                    <td><img src="data:image/jpeg;base64,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" width="100" height="100" alt="CATS"></td>
                    <td><input type="radio" name="model" value="CATS"><br /></td>
                    </tr>
                    <tr>
                    <td>Maine</td>
                    <td><img src="data:image/jpeg;base64,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" width="100" height="100" alt="Maine"></td>
                    <td><input type="radio" name="model" value="Maine"><br /></td>
                    </tr>
                    <tr>
                    <td>Scotish</td>
                    <td><img src="data:image/jpeg;base64,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" width="100" height="100" alt="Scotish"></td>
                    <td><input type="radio" name="model" value="nissan"><br /></td>
                    </tr>
                    <tr>
                    <td>Sphynx</td>
                    <td><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvYbDksR1VRA8o5uybLRt_9ZbVT6Z87O5t1dj23bRCqv594Pu9" width="100" height="100" alt="Sphynx"></td>
                    <td><input type="radio" name="model" value="Sphynx"><br /></td>
                    </tr>
                    <tr>
                    <td></td>
                    <td><input type="submit" value="Submit" /></td>
                    <td></td>
                    </tr>
                    </table>
                </form>
    '''
    return html("survey", content)


def results():
    global British_counter
    global Maine_counter
    global Scotish_counter
    global Sphynx_counter

    model = str(request.forms.get('model'))
    print(model)
    if model == "British":
        British_counter += 1
    elif model == "Maine":
        Maine_counter += 1
    elif model == "Scotish":
        Scotish_counter += 1
    elif model == "Sphynx":
        Sphynx_counter += 1

    content = '<h3>British:' + str(British_counter) + '</h3>'
    content += '<h3>Maine:' + str(Maine_counter) + '</h3>'
    content += '<h3>Scotish:' + str(Scotish_counter) + '</h3>'
    content += '<h3>Sphynx:' + str(Sphynx_counter) + '</h3>'
    content += '<a href=/survey>Back</ a>'
    return html("Results", content)


def selection_of_model():
    model = str(request.forms.get('model'))
    if model == "MALE":
        return S2000_MALE()
    elif model == "FEMALE":
        return S2000_FEMALE()


def list_page():
    content = '''  <table>\n
                     <tr>\n
                     <th>Name</th>\n
                     <th>Birth Year</th>\n
                     <th>Birth Place</th>\n
                     <th>E-mail Address</th>\n
                     <th></th>\n
                     </tr>\n
              '''

    if model == "MALE":

        title = 'MALE CLUB'

        for person in owners_of_MALE:
            content += '  <tr>\n'
            content += '    <td>' + str(person['name']) + '</td>\n'
            content += '    <td>' + str(person['model']) + '</td>\n'
            content += '    <td>' + str(person['birthplace']) + '</td>\n'
            content += '    <td>' + str(person['email']) + '</td>\n'
            content += '    <td>\n'
            content += '      <form method="GET" action="/update/' + str(person['name']) + '">\n'
            content += '        <input type="submit" value="Update" />\n'
            content += '      </form>\n'
            content += '    </td>\n'
            content += '  </tr>\n'

        content += '</table>\n'
        content += '<a href="/MALE/">Back</a>'
    elif model == "FEMALE":
        title = 'FEMALE CLUB'

        for person in owners_of_FEMALE:
            content += '  <tr>\n'
            content += '    <td>' + str(person['name']) + '</td>\n'
            content += '    <td>' + str(person['model']) + '</td>\n'
            content += '    <td>' + str(person['birthplace']) + '</td>\n'
            content += '    <td>' + str(person['email']) + '</td>\n'
            content += '    <td>\n'
            content += '      <form method="GET" action="/update/' + str(person['name']) + '">\n'
            content += '        <input type="submit" value="Update" />\n'
            content += '      </form>\n'
            content += '    </td>\n'
            content += '  </tr>\n'

        content += '</table>\n'
        content += '<a href="/FEMALE/">Back</a>'

    return html(title, content)


def search_by_name(name, people):
    for person in people:
        if person['name'] == name:
            return person


def update_page(name):
    title = 'Update'
    if model == "MALE":

        global owners_of_MALE
        person = search_by_name(name, owners_of_MALE)

        content = '<form method="POST" action="/update_submit">\n'
        content += '  Name: <input  type="text" name="name" value="' + str(person['name']) + '" readonly /><br />\n'
        content += '  Birth Year: <input type="number" name="model" value=' + str(person['model']) + ' /><br />\n'
        content += '  Birth Place: <input type="text" name="birthplace" value="' + str(
            person['birthplace']) + '" /><br />\n'
        content += '  E-mail Address: <input type="email" name="email" value="' + str(person['email']) + '" /><br />\n'
        content += '  <input type="submit" value="Update" />\n'
        content += '</form>\n'

    elif model == "FEMALE":

        global owners_of_FEMALE
        person = search_by_name(name, owners_of_FEMALE)

        content = '<form method="POST" action="/update_submit">\n'
        content += '  Name: <input  type="text" name="name" value="' + str(person['name']) + '" readonly /><br />\n'
        content += '  Birth Year: <input type="number" name="model" value=' + str(person['model']) + ' /><br />\n'
        content += '  Birth Place: <input type="text" name="birthplace" value="' + str(
            person['birthplace']) + '" /><br />\n'
        content += '  E-mail Address: <input type="email" name="email" value="' + str(person['email']) + '" /><br />\n'
        content += '  <input type="submit" value="Update" />\n'
        content += '</form>\n'

    return html(title, content)


def update_submit_page():
    title = 'JOIN MALE CLUB'
    post_request = request.POST

    name = str(post_request['name'])
    byear = int(post_request['model'])
    birthplace = str(post_request['birthplace'])
    email = str(post_request['email'])

    if model == "MALE":

        person = search_by_name(name, owners_of_MALE)
        person['name'] = name
        person['model'] = byear
        person['birthplace'] = birthplace
        person['email'] = email

        content = '<p>Updated the following person:</p>\n'
        content += '<table >\n'
        content += '  <tr>\n'
        content += '    <th>Name</th>\n'
        content += '    <th>Birth Year</th>\n'
        content += '    <th>Birth Place</th>\n'
        content += '    <th>E-mail Address</th>\n'
        content += '  </tr>\n'
        content += '  <tr>\n'
        content += '    <td>' + str(name) + '</td>\n'
        content += '    <td>' + str(byear) + '</td>\n'
        content += '    <td>' + str(birthplace) + '</td>\n'
        content += '    <td>' + str(email) + '</td>\n'
        content += '  </tr>\n'
        content += '</table>\n'
    elif model == "FEMALE":

        person = search_by_name(name, owners_of_FEMALE)
        person['name'] = name
        person['model'] = byear
        person['birthplace'] = birthplace
        person['email'] = email

        content = '<p>Updated the following person:</p>\n'
        content += '<table >\n'
        content += '  <tr>\n'
        content += '    <th>Name</th>\n'
        content += '    <th>Birth Year</th>\n'
        content += '    <th>Birth Place</th>\n'
        content += '    <th>E-mail Address</th>\n'
        content += '  </tr>\n'
        content += '  <tr>\n'
        content += '    <td>' + str(name) + '</td>\n'
        content += '    <td>' + str(byear) + '</td>\n'
        content += '    <td>' + str(birthplace) + '</td>\n'
        content += '    <td>' + str(email) + '</td>\n'
        content += '  </tr>\n'
        content += '</table>\n'
    content += '<a href="/list">Back</a>'
    return html(title, content)


def add_page():
    title = 'JOIN MALE CLUB'

    content = '<form method="POST" action="/add_submit">\n'
    content += '  Name: <input type="text" name="name" /><br />\n'
    content += '  Birth Year: <input type="number" name="model" /><br />\n'
    content += '  Birth Place: <input type="text" name="birthplace" /><br />\n'
    content += '  E-mail Address: <input type="email" name="email" /><br />\n'
    content += '  <input type="submit" value="Add" />\n'
    content += '</form>\n'

    return html(title, content)


def add_submit_page():
    title = 'JOIN US'

    post_request = request.POST
    name = str(post_request['name'])
    byear = int(post_request['model'])
    birthplace = str(post_request['birthplace'])
    email = str(post_request['email'])
    content = ""
    if model == "MALE":
        global owners_of_MALE
        owners_of_MALE += [{'name': name, 'model': byear, 'birthplace': birthplace, 'email': email}]

        content = '<p>Added the following person:</p>\n'
        content += '<table>\n'
        content += '  <tr>\n'
        content += '    <th>Name</th>\n'
        content += '    <th>Birth Year</th>\n'
        content += '    <th>Birth Place</th>\n'
        content += '    <th>E-mail Address</th>\n'
        content += '  </tr>\n'
        content += '  <tr>\n'
        content += '    <td>' + str(name) + '</td>\n'
        content += '    <td>' + str(byear) + '</td>\n'
        content += '    <td>' + str(birthplace) + '</td>\n'
        content += '    <td>' + str(email) + '</td>\n'
        content += '  </tr>\n'
        content += '</table>\n'
    elif model == "FEMALE":
        global owners_of_FEMALE
        owners_of_FEMALE += [{'name': name, 'model': byear, 'birthplace': birthplace, 'email': email}]

        content = '<p>Added the following person:</p>\n'
        content += '<table>\n'
        content += '  <tr>\n'
        content += '    <th>Name</th>\n'
        content += '    <th>Birth Year</th>\n'
        content += '    <th>Birth Place</th>\n'
        content += '    <th>E-mail Address</th>\n'
        content += '  </tr>\n'
        content += '  <tr>\n'
        content += '    <td>' + str(name) + '</td>\n'
        content += '    <td>' + str(byear) + '</td>\n'
        content += '    <td>' + str(birthplace) + '</td>\n'
        content += '    <td>' + str(email) + '</td>\n'
        content += '  </tr>\n'
        content += '</table>\n'

    content += '<a href="/list">Back</a>'
    return html(title, content)


######################################################################################################################################################
######################################################################################################################################################


route('/', 'GET', index)
route('/login/', 'POST', login)
route('/signup/', 'GET', signup)
route('/signup_complete', 'POST', signup_complete)
route('/selection_of_model/', 'POST', selection_of_model)
route('/homepage/', 'GET', my_website)

route('/update/<name>', 'GET', update_page)
route('/list', 'GET', list_page)
route('/update_submit', 'POST', update_submit_page)
route('/add', 'GET', add_page)
route('/add_submit', 'POST', add_submit_page)

route('/upgrading', 'GET', S2000_PARTS)
route('/survey', 'GET', survey)
route('/results', 'POST', results)

route('/FEMALE/', 'GET', S2000_FEMALE)
route('/MALE/', 'GET', S2000_MALE)

route('/assignment3/', 'GET', index)
#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
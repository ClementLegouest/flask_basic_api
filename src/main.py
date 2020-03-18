from flask_api import FlaskAPI
import mysql.connector

app = FlaskAPI(__name__)


# database connection
def connect_database():
    database = mysql.connector.connect(
        host="localhost",
        user="contact",
        passwd="contact",
        database='contact'
    )
    return database


def get_cursor(database):
    return database.cursor()


# root
@app.route('/', methods=['GET'])
def get_root():
    return {'status': 200,
            'Hello': 'World'}


@app.route('/', methods=['POST', 'PUT', 'PATCH', 'DELETE', 'COPY', 'HEAD', 'OPTIONS',
                         'LINK', 'UNLINK', 'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW'])
def denied_root():
    return {'status': 403,
            'Hello': 'forbidden'}


# contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    database = connect_database()
    cursor = get_cursor(database)

    cursor.execute("SELECT `ID`, `firstname`, `lastname`, `phone_number` FROM `contact` WHERE 1")
    result = cursor.fetchall()

    cursor.close()
    database.close()

    return result


@app.route('/contacts', methods=['POST', 'PUT', 'PATCH', 'DELETE', 'COPY', 'HEAD', 'OPTIONS',
                                 'LINK', 'UNLINK', 'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW'])
def denied_contacts():
    return {'status': 403,
            'Hello': 'forbidden'}


# contact
@app.route('/contact/<int:uid>', methods=['GET'])
def get_contact(uid):

    database = connect_database()
    cursor = get_cursor(database)

    cursor.execute("SELECT `firstname`, `lastname`, `phone_number` FROM `contact` WHERE `ID` = " + str(uid))
    result = cursor.fetchall()

    cursor.close()
    database.close()

    return result


@app.route('/contact', methods=['POST'])
def post_contact():
    return {'status': 200,
            'data':
                {'lastname': 'Le_Lastname',
                 'firstname': 'Le_Firstname'},
            'info': 'Contact Created'
            }


@app.route('/contact/<int:uid>', methods=['DELETE'])
def delete_contact(uid):
    return {'status': 200,
            'data':
                {'uid': uid,
                 'lastname': 'Le_Lastname',
                 'firstname': 'Le_Firstname'},
            'info': 'Contact ' + str(uid) + ' deleted'
            }


if __name__ == '__main__':
    app.run(debug=True)

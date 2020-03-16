from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/', methods=['GET'])
def get_root():
    return {'status': 200,
            'Hello': 'World'}


@app.route('/', methods=['POST', 'PUT', 'PATCH', 'DELETE', 'COPY', 'HEAD', 'OPTIONS',
                         'LINK', 'UNLINK', 'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW'])
def denied_root():
    return {'status': 403,
            'Hello': 'forbidden'}


if __name__ == '__main__':
    app.run(debug=True)

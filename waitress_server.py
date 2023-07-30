from waitress import serve
from app import app

if __name__ == '__main__':
    # By using app.wsgi_app, you get the WSGI callable for your Flask app.
    #http://localhost:8080/
    serve(app.wsgi_app, host='0.0.0.0', port=8080)
from testweb import create_app

application = create_app()

# gunicorn -b 0.0.0.0:8000 -t 1000 application:application

if __name__ == '__main__':
    application.run(host='0.0.0.0',
        port=8000, threaded=True, debug=True)
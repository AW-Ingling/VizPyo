# viz_server.py

# Resources:
#
# To shutdown the Flask server see these instructions. We need to add a message to the subprocesss:
# http://flask.pocoo.org/snippets/67/



# stuff
from flask import Flask, request
from flask_restful import Resource, Api
# our stuff
import pyowrap

app = Flask(__name__)
api = Api(app)


class PyoClasses(Resource):
    def get(self):
        return pyowrap.get_classes()


api.add_resource(PyoClasses, '/classes')


def start():
    app.run(debug=True, use_reloader=False)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    print("launching server from __main__")
    start()




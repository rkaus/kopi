from flask import Flask
from flask import (request,
                   redirect,
                   url_for,
                   session,
                   render_template)

from uuid import uuid1


app = Flask(__name__,static_url_path='')
# app = Flask(__name__)


def create_user():
    user = session.get('user','not a user')
    if user == 'not a user':
        session['user'] = str(uuid1())
		session.permanent = True



@app.route('/')
def index():

	if 'user' not in session.keys():
		create_user()
    # return app.send_static_file('index.html')
    return render_template('index.html')


# @app.route('/store')
# def status():
#     assert 1 == 1, "one equals one"
#     status = {'healthy':True}
#     return jsonify(status)
#
# @app.route('/store/<string:productName>')
# def personalized_welcome(productName):
#     return productName

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    

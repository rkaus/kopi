from flask import Flask, render_template

app = Flask(__name__,static_url_path='')
# app = Flask(__name__)


@app.route('/')
def index():
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

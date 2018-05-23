import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    paragraph = {'body': 'Hey there!'}
    return render_template('index.html', header='Tail', paragraph=paragraph)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

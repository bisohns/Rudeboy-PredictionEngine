import flask
from utils import get_predictions

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(CURRENT_DIR, "templates")
app = flask.Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        input_data = request.json['comment']
        preds = get_predictions(input_data)
        return flask.jsonify(preds)
    except:
        return "JSON containing 'comment' key must be passed", 400

if __name__ == "__main__":
    #locally run debug
    app.run(debug=True, port='8008')

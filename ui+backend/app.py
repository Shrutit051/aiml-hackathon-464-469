from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')

# Load both models
nb_model = joblib.load('news_detector_nb_model.pkl')
lr_model = joblib.load('news_detector_lr_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news_text = data.get('text', '')

    if not news_text.strip():
        return jsonify({'error': 'No text provided'}), 400

    # Predict using Naive Bayes
    nb_pred = nb_model.predict([news_text])[0]
    nb_conf = nb_model.predict_proba([news_text])[0]
    nb_score = max(nb_conf) * 100

    # Predict using Logistic Regression
    lr_pred = lr_model.predict([news_text])[0]
    lr_conf = lr_model.predict_proba([news_text])[0]
    lr_score = max(lr_conf) * 100

    # Choose the result with higher confidence
    if nb_score >= lr_score:
        best_pred, best_score, used_model = nb_pred, nb_score, "Naive Bayes"
    else:
        best_pred, best_score, used_model = lr_pred, lr_score, "Logistic Regression"

    result = {
        'prediction': '✅ Real News' if best_pred == 1 else '❌ Fake News',
        'confidence': f"{best_score:.2f}%",
        'model_used': used_model
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

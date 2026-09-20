from flask import Flask, render_template, request
import os
import sys

# Add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from networksecurity.pipeline.prediction import NetworkSecurityPredictor

app = Flask(__name__)

model_path = os.path.join(
    "Artifacts",
    "model_trainer",
    "trained_model.pkl"
)

predictor = NetworkSecurityPredictor(model_path)

feature_names = [
    "having_IP_Address",
    "URL_Length",
    "Shortining_Service",
    "having_At_Symbol",
    "double_slash_redirecting",
    "Prefix_Suffix",
    "having_Sub_Domain",
    "SSLfinal_State",
    "Domain_registeration_length",
    "Favicon",
    "port",
    "HTTPS_token",
    "Request_URL",
    "URL_of_Anchor",
    "Links_in_tags",
    "SFH",
    "Submitting_to_email",
    "Abnormal_URL",
    "Redirect",
    "on_mouseover",
    "RightClick",
    "popUpWidnow",
    "Iframe",
    "age_of_domain",
    "DNSRecord",
    "web_traffic",
    "Page_Rank",
    "Google_Index",
    "Links_pointing_to_page",
    "Statistical_report"
]


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        input_data = {}

        for feature in feature_names:
            input_data[feature] = int(request.form[feature])

        prediction = predictor.predict(input_data)

        if prediction == 1:
            result = "Legitimate Website"
        else:
            result = "Phishing Website"

    return render_template(
        "index.html",
        feature_names=feature_names,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
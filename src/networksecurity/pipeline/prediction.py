import os
import joblib
import pandas as pd


class NetworkSecurityPredictor:

    def __init__(self, model_path):
        self.model_path = model_path
        self.model = joblib.load(model_path)

    def predict(self, input_data):

        if isinstance(input_data, dict):
            input_data = pd.DataFrame([input_data]).values

        prediction = self.model.predict(input_data)

        return prediction[0]


if __name__ == "__main__":

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

    print("\nEnter values for the website features.")
    print("Allowed values: -1, 0, or 1\n")

    input_data = {}

    for feature in feature_names:
        value = int(input(f"{feature}: "))
        input_data[feature] = value

    result = predictor.predict(input_data)

    print("\nPrediction:", result)

    if result == 1:
        print("Result: Legitimate website")
    else:
        print("Result: Phishing website")
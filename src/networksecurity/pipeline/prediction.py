import os
import joblib
import pandas as pd


class NetworkSecurityPredictor:

    def __init__(self, model_path):
        self.model_path = model_path
        self.model = joblib.load(model_path)

    def predict(self, input_data):

        if isinstance(input_data, dict):
            input_data = pd.DataFrame([input_data])

        prediction = self.model.predict(input_data)

        return prediction[0]


if __name__ == "__main__":

    model_path = os.path.join(
        "Artifacts",
        "model_trainer",
        "trained_model.pkl"
    )

    predictor = NetworkSecurityPredictor(model_path)

    sample_data = {
        "having_IP_Address": 1,
        "URL_Length": 1,
        "Shortining_Service": 1,
        "having_At_Symbol": 1,
        "double_slash_redirecting": 1,
        "Prefix_Suffix": -1,
        "having_Sub_Domain": 1,
        "SSLfinal_State": 1,
        "Domain_registeration_length": 1,
        "Favicon": 1,
        "port": 1,
        "HTTPS_token": 1,
        "Request_URL": 1,
        "URL_of_Anchor": 1,
        "Links_in_tags": 1,
        "SFH": 1,
        "Submitting_to_email": 1,
        "Abnormal_URL": 1,
        "Redirect": 1,
        "on_mouseover": 1,
        "RightClick": 1,
        "popUpWidnow": 1,
        "Iframe": 1,
        "age_of_domain": 1,
        "DNSRecord": 1,
        "web_traffic": 1,
        "Page_Rank": 1,
        "Google_Index": 1,
        "Links_pointing_to_page": 1,
        "Statistical_report": 1
    }

    result = predictor.predict(sample_data)

    print("Prediction:", result)
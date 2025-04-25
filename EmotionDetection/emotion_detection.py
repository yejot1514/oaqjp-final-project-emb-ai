import requests, json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    emotion_response = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_response['anger']
    disgust_score = emotion_response['disgust']
    fear_score = emotion_response['fear']
    joy_score = emotion_response['joy']
    sadness_score = emotion_response['sadness']
    # Returning a dictionary containing emotion analysis results
    dominant_emotion = 'anger'
    dominant_emotion_score = emotion_response[dominant_emotion]
    for key, value in emotion_response.items():
        if(value > dominant_emotion_score):
            dominant_emotion_score = value
            dominant_emotion = key
    
    emotion_dict = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
    return emotion_dict
    

    
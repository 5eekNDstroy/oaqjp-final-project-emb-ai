import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotion_predictor = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictor.items(), key=lambda x: x[1])[0]
        
        # Construct the formatted output dictionary
        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return output
    # if response.status_code == 200:
    #     label = formatted_response['documentSentiment']['label']
    #     score = formatted_response['documentSentiment']['score']
    # elif response.status_code == 500:
    #     label = None
    #     score = None
    # return {'label': label, 'score': score}
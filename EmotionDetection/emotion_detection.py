import requests
import json

def emotion_detector(text_to_analyze):
    # Get emotion detect details
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    
    # Get Emotion Scores
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']

    # Get Dominant Emotion
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions

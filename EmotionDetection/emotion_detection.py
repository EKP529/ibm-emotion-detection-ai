import requests
import json

def emotion_detector(text_to_analyze):
    request = {
        "url": 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        "headers": {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        "json": { "raw_document": { "text": text_to_analyze } }
    }
    response = requests.post(request['url'], json=request['json'], headers=request['headers'])
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
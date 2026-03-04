import requests
import json

def emotion_detector(text_to_analyze):
    # Определение URL и заголовков для API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Формирование входного JSON
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Отправка POST-запроса
    response = requests.post(url, json=myobj, headers=headers)
    
    # Возвращаем текстовый атрибут ответа
import requests

# Configurações
translator_endpoint = "https://api.cognitive.microsofttranslator.com/translate"
translator_key = "YOUR_TRANSLATOR_KEY"
region = "YOUR_REGION"

# Função de tradução
def translate_text(text, from_lang, to_lang):
    headers = {
        "Ocp-Apim-Subscription-Key": translator_key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-Type": "application/json"
    }
    body = [{"text": text}]
    params = {"api-version": "3.0", "from": from_lang, "to": to_lang}
    
    response = requests.post(translator_endpoint, headers=headers, params=params, json=body)
    return response.json()

# Exemplo de uso
translated = translate_text("Hello, world!", "en", "pt")
print(translated[0]['translations'][0]['text'])

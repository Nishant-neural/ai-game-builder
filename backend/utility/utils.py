import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
# MODEL = "llama3.2:3b"  # change if needed

def call_ollama(system_prompt: str, user_prompt: str, MODEL = "llama3.2:3b" , retries = 3):
    for attempt in range(retries):
        try:
            response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "stream": False ,
            "temperature" : 0.3
        },
        timeout = 180
    )
            data = response.json()
            return data["message"]["content"]    
        
        except Exception as e:
                if attempt == retries - 1:
                    raise e

   
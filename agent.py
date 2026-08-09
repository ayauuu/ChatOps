import requests
import json

def analyser_avec_ollama(prompt_utilisateur):
    url = "http://localhost:11434/api/generate"
    
    payload = {
    "model": "phi3",  # Garde ton modèle (phi3 ou llama3)
    "prompt": f"Agis en tant qu'expert DevOps. Analyse ce problème d'infrastructure et donne un diagnostic très court (maximum 5 lignes) et une solution claire : {prompt_utilisateur}",
    "stream": False
}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "Pas de réponse du modèle.")
        else:
            return "Erreur de communication avec le moteur Ollama."
    except Exception as e:
        return f"Erreur technique : {e}"
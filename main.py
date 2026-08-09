from fastapi import FastAPI
from pydantic import BaseModel
from agent import analyser_avec_ollama

app = FastAPI(title="Smart ChatOps Backend")

class RequeteAI(BaseModel):
    message: str

@app.post("/chat")
def traiter_message(req: RequeteAI):
    # Simulation de l'étape d'interrogation de l'infrastructure (Kubernetes)
    # Dans la version complète, c'est ici qu'on récupère les vrais logs du cluster
    logs_simules = "[ERROR 500] Pod auth-service en échec : Database timeout."
    
    # On combine les logs et la question de l'utilisateur pour l'IA
    prompt_complet = f"Question de l'utilisateur : {req.message}\nLogs techniques : {logs_simules}"
    
    # Appel de l'IA
    diagnostic_ia = analyser_avec_ollama(prompt_complet)
    
    return {
        "status": "success",
        "diagnostic": diagnostic_ia
    }
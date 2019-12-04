import os
from bigml.ensemble import Ensemble
from bigml.api import BigML

CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(CURRENT_DIR, "cache")

api = BigML("deven96", "81795cceca568fff4115d5c047071728a0700673", storage=CACHE_DIR)
predictions = {
        "toxicity": "",
        "identity_hatred": "",
        "threat": "",
        "obscene": "",
        "severe_toxicity": "",
        "insult": "",
        }
ensembles = predictions.copy()
ensembles["toxicity"] = Ensemble('ensemble/5ddd1a3f1efc925827001f7a', api)
ensembles["identity_hatred"] = Ensemble('ensemble/5ddd1b6f5a213904ee0000ca', api)
ensembles["threat"] = Ensemble('ensemble/5ddd282959f5c31acc001a01', api)  
ensembles["obscene"] = Ensemble('ensemble/5ddd1ad959f5c31acc001999', api)
ensembles["severe_toxicity"] = Ensemble('ensemble/5ddd1aab1efc925827001f7d', api)
ensembles["insult"] = Ensemble('ensemble/5ddd1b3c5e269e4886001b8c', api)

def get_predictions(input_data):
    """
    Returns the strings gotten from each toxicity 
    api
    """
    
    for key, ensemble in ensembles.items():
        predictions[key] = ensemble.predict({"comment_text":input_data}, full=True)

    return predictions

import os
import pickle
from bigml.ensemble import Ensemble
from bigml.api import BigML

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(CURRENT_DIR, "cache")
CACHE = os.path.join(CACHE_DIR, "emblem-dict.pkl")

if not os.path.exists(CACHE):
    api = BigML("deven96", "81795cceca568fff4115d5c047071728a0700673", domain="bigml.io")
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
    
    with open(CACHE, "wb+") as stream:
        pickle.dump(ensembles, stream)
else:
    with open(CACHE, "rb") as stream:
        ensembles = pickle.load(stream)

def get_predictions(input_data):
    """
    Returns the strings gotten from each toxicity 
    api
    """
    
    for key, ensemble in ensembles.items():
        predictions[key] = ensemble.predict({"comment_text":input_data}, full=True)

    return predictions

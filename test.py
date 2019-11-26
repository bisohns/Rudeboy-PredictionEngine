from bigml.ensemble import Ensemble
# Downloads and generates a local version of the ensemble, if it
# hasn't been downloaded previously.
from bigml.api import BigML
ensemble = Ensemble('ensemble/5ddd1a3f1efc925827001f7a',
                    api=BigML("deven96",
                              "81795cceca568fff4115d5c047071728a0700673",
                              domain="bigml.io"))
# To make predictions fill the desired input_data in next line.
input_data = {}
ret = ensemble.predict({'comment': "fuck you cunt"}, full=True)
print(ret)

import pandas as pd
import numpy as np

a = pd.read_table('freq', sep='\s+', header=None, index_col=0, engine='python')

acustic1 = a.loc[:,5]
acustic2 = a.loc[:,6]
acustic3 = a.loc[:,7]
acustic = acustic1.tolist() + acustic2.tolist() + acustic3.tolist()

minf = min(acustic) * 0.188369895509244
maxf = max(acustic) * 0.188369895509244
detf = (minf + maxf)/1000

nDos = [(x*0.188369895509244)//(detf) for x in acustic]
result = pd.value_counts(nDos)
freq1 = result.index.values
freq = np.array([detf*x for x in freq1])

val = np.array(result.tolist())
sumVal = sum(val)
dosVal = np.array([3*x/(detf*sumVal) for x in val])
combined = list(np.vstack((freq, dosVal)).T)
add =[[i*detf, 0] for i in range(1000) if float(i) not in freq1]
combined = combined+ add
combined.sort(key=lambda x: x[0])
np.savetxt('SlackModelOutput/Slack.Dos',combined)




import pandas as pd
import copy as cp

def elimination(obser):
    size = len(obser.columns)-1
    #initialize specific and general hypothesis
    spec_hyp=[0]*size
    gen_hyp=['?']*size
    
    for index, row in obser.iterrows():
        instance = row[:-1].tolist()
        label = row[-1]

        if label == 'Y':
            for i in range(size):
                if spec_hyp[i]==0:spec_hyp[i]=instance[i]
            for i in range(size):
                if gen_hyp[i] != '?' and gen_hyp[i]!=instance[i]:gen_hyp[i]='?'
        else:
            temp_spec = cp.deepcopy(spec_hyp)
            for i in range(size):
                if spec_hyp[i] != '?' and spec_hyp[i]!=instance[i]:temp_spec[i]='?'
            spec_hyp=temp_spec
            for i in range(size):
                if spec_hyp[i]=='?':gen_hyp[i]='?'
        print(spec_hyp,gen_hyp)
    return spec_hyp,gen_hyp

# Load the CSV file
csv_file_path = 'candidate_set.csv'
# csv_file_path = 'exp2.csv'
observations = pd.read_csv(csv_file_path)
#print(observations.iterrows)
#print(observations.columns)

specific,general = elimination(observations)
print("Specification",specific)
print("General",general)


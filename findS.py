'''
The Find-S algorithm is a simple, incremental machine learning algorithm 
used for concept learning in the context of machine learning and 
artificial intelligence. 
It is specifically designed for learning from examples 
in a supervised learning setting.
'''
import csv

def find_s(examples):
    print(examples)
    h = [0]*len(examples[0][:-1])
    print(h)
    for x in examples:
        if x[-1] == 'Yes':  # Check if positive example
            for i in range(len(x)-1):
                print(x[i],h[i])
                if h[i]==0:
                    h[i]=x[i]
                elif h[i] != x[i]:
                    h[i] = '?'
                print(h)
            print(h)
    return h


# def find_s_algorithm(training_data):
#     attributes = training_data[0][:-1]
#     print(attributes)
#     hypothesis = ['0'] * len(attributes)
#     print(hypothesis)

#     for example in training_data[1:]:
#         if example[-1] == 'Yes':  # Positive example
#             print(example)
#             for i, (hypo_attr, ex_attr) in enumerate(zip(hypothesis, example[:-1])):
#                 print(i,(hypo_attr,ex_attr))
#                 if hypo_attr == '0':
#                     hypothesis[i] = ex_attr
#                 elif hypo_attr != ex_attr:
#                     hypothesis[i] = '?'
#                 print(hypothesis)
#             print(hypothesis)

#     return hypothesis

# Read training data from CSV file
file=open('training_data.csv','r')
csv_reader = csv.reader(file)
data=list(csv_reader)


# Demonstrate Find-S algorithm
result_hypothesis = find_s(data[1:])

# Display results
print("Most specific hypothesis:")
print(result_hypothesis)










# import csv

# def load_csv(filename):
#     lines=csv.reader(open(filename,'r'))
#     data_set=list(lines)
#     return data_set
    
# datum=load_csv('training_data.csv')
# attributes=['Outlook','Temperature','Humidity','Windy','PlayTennis']
# hypothesis=['0'] * len(attributes)
# print(hypothesis)

# for i in range(len(datum)):
#     target=datum[i][-1]
#     # print(target)
#     if target=='Yes':
#         for j in range(len(attributes)):
#             if hypothesis[j]=='0':
#                 hypothesis[j]=datum[i][j]

# print(hypothesis)
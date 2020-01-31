import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

with open("words/words.json") as file:
    data = json.load(file)

try:
    raise
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in list(data.keys()):
        for pattern in data[intent]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent)

        if intent not in labels:
            labels.append(intent)

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    # with open("data.pickle", "wb") as f:
    #     pickle.dump((words, labels, training, output), f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 100)
net = tflearn.fully_connected(net, 100)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# try:
model.load("model.tflearn")
# except:
# model.fit(training, output, n_epoch=50, batch_size=16, show_metric=True)
# model.save("model.tflearn")

def input_for_model(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    s_words = [s for s in s_words if s != ","]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return numpy.array(bag)



def results(bagWords):
    prediction = model.predict([bagWords])
    index = numpy.argmax(prediction)
    tag = labels[index]
    print(prediction[0][index])
    if prediction[0][index] > .40:
        return tag
    else: 
        return "neutral or unsure"

print(results(input_for_model("Its so depressing that Kobe Bryant and daughter passed away. Im heartbroken", words)))
# from TwitterBot import tweets as a , messages as b 
# for b in a:
#     print(results(input_for_model(b, words)))

# for a in b:
#     print(results(input_for_model(a, words)))
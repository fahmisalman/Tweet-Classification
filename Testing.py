import csv
import numpy as np
import NaiveBayes as nb
import EmotionTrain as et
import GenderTrain as gt
import Posterior as post


if __name__ == '__main__':
    likelihood = np.array(list(csv.reader(open("Model/Emotion/likelihood_emotion.csv"), delimiter=",")))\
        .astype("float")
    prior = np.array(list(csv.reader(open("Model/Emotion/prior_emotion.csv"), delimiter=",")))\
        .astype("float")
    label = np.array(list(csv.reader(open("Model/Emotion/label_emotion.csv"), delimiter=",")))
    words = np.array(list(csv.reader(open("Model/Emotion/words_emotion.csv"), delimiter=",")))

    words = words.tolist()
    label = label.tolist()

    x_test, y_test = et.load_data()
    for i in range(len(x_test)):
        x_test[i] = et.preprocessing(x_test[i])

    i = 0
    while i < len(x_test):
        if len(x_test[i]) == 0:
            x_test.pop(i)
            y_test.pop(i)
        else:
            i += 1

    result = []
    for i in range(len(x_test)):
        result.append(nb.testing(x_test[i], label[0], words[0], prior[0], likelihood))

    correct = 0
    for i in range(len(result)):
        if result[i] == y_test[i]:
            correct += 1
    print('Emotion accuracy:', correct/len(result))

    likelihood = np.array(list(csv.reader(open("Model/Gender/likelihood_gender.csv"), delimiter=","))) \
        .astype("float")
    prior = np.array(list(csv.reader(open("Model/Gender/prior_gender.csv"), delimiter=","))) \
        .astype("float")
    label = np.array(list(csv.reader(open("Model/Gender/label_gender.csv"), delimiter=",")))
    words = np.array(list(csv.reader(open("Model/Gender/words_gender.csv"), delimiter=",")))

    words = words.tolist()
    label = label.tolist()

    x_test, y_test = gt.load_data()
    for i in range(len(x_test)):
        x_test[i] = gt.preprocessing(x_test[i])

    i = 0
    while i < len(x_test):
        if len(x_test[i]) == 0:
            x_test.pop(i)
            y_test.pop(i)
        else:
            i += 1

    result = []
    for i in range(len(x_test)):
        result.append(nb.testing(x_test[i], label[0], words[0], prior[0], likelihood))

    correct = 0
    for i in range(len(result)):
        if result[i] == y_test[i]:
            correct += 1
    print('Gender accuracy:', correct / len(result))

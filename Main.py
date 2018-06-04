import Preprocessing as pre
import csv
import NaiveBayes as nb


def preprocessing(sentence):
    sentence = pre.caseFolding(sentence)
    token = pre.tokenization(sentence)
    token = pre.stopwordRemoval(token)
    token = pre.lemmatization(token)
    return token


def load_data():
    x = []
    y = []
    with open('data_emotion.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x.append(row[0])
            y.append(row[1])
    return x, y


def save_data(location, obj):
    with open(location, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(obj)


if __name__ == '__main__':

    # Load Data
    x_train, y_train = load_data()

    # Preprocessing Data
    for i in range(len(x_train)):
        x_train[i] = preprocessing(x_train[i])

    i = 0
    while i < len(x_train):
        if len(x_train[i]) == 0:
            x_train.pop(i)
            y_train.pop(i)
        else:
            i += 1

    # Training
    prior, likelihood, label_list, words_list = nb.training(x_train, y_train)

    save_data('prior.csv', prior)
    save_data('likelihood.csv', likelihood)
    save_data('label.csv', label_list)
    save_data('words.csv', words_list)

    # Testing
    # result = []
    # for i in range(len(x_train)):
    #     result.append(nb.testing(x_train[i], label_list, words_list, prior, likelihood))
    #
    # # Accuracy Testing
    # correct = 0
    # for i in range(len(y_train)):
    #     if result[i] == y_train[i]:
    #         correct += 1
    #
    # print(correct)
    # print(correct/len(y_train))

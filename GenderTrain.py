import Preprocessing as pre
import csv
import NaiveBayes as nb
import TweetCleaning as tc


def preprocessing(sentence):
    sentence = pre.caseFolding(sentence)
    token = pre.tokenization(sentence)
    token = pre.stopwordRemoval(token)
    token = pre.lemmatization(token)
    return token


def load_data():
    x = []
    y = []
    with open('Dataset/data_gender.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            y.append(row['gender'])
            x.append(row['text'])
    return x, y


def save_data1(location, obj):
    with open('Model/Gender/%s' % location, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(obj)


def save_data2(location, obj):
    with open('Model/Gender/%s' % location, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([obj])


if __name__ == '__main__':

    x_train, y_train = load_data()

    for i in range(len(x_train)):
        x_train[i] = tc.url_removal(tc.hashtag_removal(tc.at_removal(x_train[i])))
        x_train[i] = preprocessing(x_train[i])

    i = 0
    while i < len(x_train):
        if len(x_train[i]) == 0:
            x_train.pop(i)
            y_train.pop(i)
        else:
            i += 1

    prior, likelihood, label_list, words_list = nb.training(x_train, y_train)

    save_data2('prior_gender.csv', prior)
    save_data1('likelihood_gender.csv', likelihood)
    save_data2('label_gender.csv', label_list)
    save_data2('words_gender.csv', words_list)

import math


label_list = []
words_list = []
prior = []
likelihood = []


def prior_probability(y, y_list):
    p = [0] * len(y_list)
    for i in range(len(y_list)):
        for j in range(len(y)):
            if y_list[i] == y[j]:
                p[i] += 1
    total_p = sum(p)
    for i in range(len(p)):
        p[i] /= total_p
    return p


def likelihood_probability(x, y, x_list, y_list):
    l = []
    for i in range(len(x_list)):
        a = []
        for j in range(len(y_list)):
            temp = 0
            for k in range(len(x)):
                if y[k] == y_list[j]:
                    temp += x[k].count(x_list[i])
            temp += 1
            a.append(temp)
        l.append(a)
    total_l = [0] * len(y_list)
    for i in range(len(l)):
        for j in range(len(l[i])):
            total_l[j] += l[i][j]
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] /= total_l[j]
    return l


def training(x_train, y_train):
    label_list = list(set(y_train))

    prior = prior_probability(y_train, label_list)

    bag = []
    for i in range(len(x_train)):
        bag += x_train[i]

    words_list = list(set(bag))
    likelihood = likelihood_probability(x_train, y_train, words_list, label_list)

    return prior, likelihood, label_list, words_list


def testing(x, label_list, words_list, prior, likelihood):
    result = []
    for i in range(len(label_list)):
        temp = 0
        for j in range(len(x)):
            if x[j] in words_list:
                temp += math.log(likelihood[words_list.index(x[j])][i])
        temp += math.log(prior[i])
        result.append(temp)

    return label_list[result.index(max(result))]

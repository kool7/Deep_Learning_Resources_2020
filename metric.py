from sklearn.metrics import accuracy_score

def accuray(y_true, y_pred):

    counter = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            counter += 1

    return counter / len(y_true)

#####################################################
def true_positive(y_true, y_pred):
    
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1

    return tp

def true_negative(y_true, y_pred):

    tn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 0:
            tn += 1

    return tn

def false_positive(y_true, y_pred):

    fp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 1:
            fp += 1

    return fp

def false_negative(y_true, y_pred):

    fn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 0:
            fn += 1

    return fn
######################################################

def precision(y_true, y_pred):

    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    return tp/ (tp + fp)

def recall(y_true, y_pred):

    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    return tp / (tp + fn)

def f1_score(y_true, y_pred):

    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * p * r / (p + r)


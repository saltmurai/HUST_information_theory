import numpy as np

def self_information(p):
    return -np.log2(p)

def entropy(p):
    out = np.nansum(-p * np.log2(p))
    return out

def joint_entropy(p_xy):
    out = np.nansum(-p_xy * np.log2(p_xy))
    return out

def joint_prob(p_y_given_x, p_x):
    p_xy = p_y_given_x * p_x
    return p_xy

def conditional_prob(p_xy, p_x):
    p_y_given_x = p_xy / p_x
    return p_y_given_x

def conditional_entropy(p_xy, p_x):
    p_y_given_x = p_xy / p_x
    out = np.nansum( -p_xy * np.log2(p_y_given_x))
    return out

def mutual_information(p_xy, p_x, p_y):
    p = p_xy / (p_x * p_y)
    out = np.nansum(p_xy * np.log2(p))
    return out

def cross_entropy(y_hat, y):
    ce = - np.log(y_hat[range(len(y_hat)), y])
    return ce.mean()

from test import *
from numpy import array as na
def main():
    p_x = na([1/3, 1/3, 1/3])
    p_ygx = na([[2/3, 1/6, 1/6], [1/6, 2/3, 1/6], [1/6, 1/6, 2/3]])
    p_xy = joint_prob(p_ygx, p_x)
    p_y = np.sum(p_xy, axis=0)
    p_xgy = conditional_prob(p_xy, p_x)
    h_x = entropy(p_x)
    h_y = entropy(p_y)
    h_xy = joint_entropy(p_xy)
    h_ygx = conditional_entropy(p_xy, p_x)
    h_xgy = conditional_entropy(p_xy, p_y)
    i_xy = mutual_information(p_xy, p_x, p_y)

    print("P_xy:")
    print(p_xy)
    print("---------------------------------------------")
    print("P_y:")
    print(p_y)
    print("---------------------------------------------")
    print("P_x_given_y")
    print(p_xgy)
    print("---------------------------------------------")
    print("P_y_given_x")
    print(p_ygx)
    print("---------------------------------------------")
    print("H_x = " + str(h_x))
    print("H_y = " + str(h_y))
    print("H_xy = " + str(h_xy))
    print("H_xgy = H_xy - H_y = " + str(h_xgy))
    print("H_ygx = H_xy - H_x = " + str(h_ygx))
    print("I_xy = H_x + H_y - H_xy = " + str(i_xy))

    

if __name__ == '__main__':
    main()
import pandas as pd
import numpy as np



class NetworkLayer(object):
    def __init__(self, Weight, input, bias, n_hidden, n_input ):
        network = np.zeros(n_hidden)
        self.Weight = Weight
        self.input = input
        sum = 0
        """ Buat komputasi untuk menghitung jumlah network """
        for i in range(0,n_hidden):
            for j in range(0,n_input + 1):

                if j==n_input :
                    sum += self.Weight[i][j] * bias                
                else:
                    sum += self.Weight[i][j] * self.input[j]

            network[i] = sum
            print( (" %i , Network %f ") % (i,network[i]))
            sum = 0

def test_network():

    n_hidden = 3
    input = np.random.rand(100)
    bias = 100
    n_input = 4
    Weight = np.random.rand(n_hidden, n_input + 1)

    print("================INPUT==========================")
    print(input)
    print("================WEIGHT==========================")
    print(Weight)

    create_net = NetworkLayer(
        Weight,
        input,
        bias,
        n_hidden,
        n_input
    )




if __name__ == '__main__':
    test_network()

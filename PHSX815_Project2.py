# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:30:21 2021

@author: d338c921
"""

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: \n -sample_size [Std. Normal disribution sample size] \n -Nexp [# of experiments] \n -n [binomial distribution sample size] \n -prob [probability of the binimial distribution] \n -output_file [filename]")
        print
        sys.exit(1)

  
    # default number of sample points
    sample_size = 100
    
    #default number of experiments
    Nexp = 10
    
    #default binomial distribution sample size
    n = 10
    
    #default binomial distribution probability
    prob = 0.5
    
    # output file defaults
    doOutputfile = False

    # read the user-provided values from the command line (if there)
    if '-sample_size' in sys.argv:
        p = sys.argv.index('-sample_size')
        sample_size = int(sys.argv[p+1])
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int((sys.argv[p+1]))
    if '-n' in sys.argv:
        p = sys.argv.index('-n')
        n = int((sys.argv[p+1]))
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        prob = int((sys.argv[p+1]))
    if '-output_file' in sys.argv:
        p = sys.argv.index('-output_file')
        output_file = str(sys.argv[p+1])
        doOutputfile = True

#Need to sample from a distribution with at least one configurable parameter (to be determined via user input) such that the output is an integer
#Generate random numbers from a binomial distribution with parameters n and p; this constructs an array of size =  sample size
    DOF = stats.binom.rvs(n, prob, size = Nexp)
    
    #create empty array to store the N chi-squared distributions
    chi_data = np.ndarray((len(DOF), sample_size))
    
    for i in range(len(DOF)):
        #create the standard normal distributions according to the specified sample size/degrees of freedom
        data_gaussian = np.random.normal(0, 1, size= (sample_size, DOF[i]))
        #create the chi_square distribution from the gaussian distributions; sum of the squares over the # of DOF
        data_chi = np.sum(data_gaussian**2, axis = 1)
        chi_data[i, :] = data_chi

    #output the file to given filename if provided; else print the data
    if doOutputfile:
        np.savetxt(output_file, chi_data)
        
    # #calculate then print: mean, variance, ...
    mean_arr = []
    variance_arr = []
    
    for i in range(len(DOF)):
        mean_arr = np.append(mean_arr, np.mean(chi_data[i]))
        #Theoretically, the mean should be equal to the number of degrees of freedom
        variance_arr = np.append(variance_arr, np.var(chi_data[i]))
    print("Randomly generated array of Degrees of Freedom: (using a Binomial Distribution)")
    print(DOF)
    print("\n")
    print("Calculated mean for each randomly generated Chi-Square Distribution:")
    print(mean_arr)
    print("\n")
    print("Calculated variance for each randomly generated Chi-Square Distribution: ")
    print(variance_arr)
        
import sys
import math

#load the weights
model_weights = []
with open("weights.txt", 'r') as file:
    for i in file:
        model_weights.append(math.floor(float(i)))





def main():
    
    input_num = float(sys.argv[1]) #passed using command line 
    model_output = model_weights[0] * input_num + model_weights[1]

    with open("output.txt", "a") as output_file:
        output_file.write(str(model_output) + "\n")

    

    return None



if __name__ == '__main__':
    main()
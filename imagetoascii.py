import cv2
import time
import sys 


'''
Convert an image to characters based on the brightness level and write the result to a file.
requires cv2 library

'''




def ImageToAscii(image_path:str,size:tuple,output_file_name):


    try:
        img = cv2.imread(image_path,0) #read image to 2d array
        x = len(img[1]) #image width
        y = len(img) #image height
    except: #image not found
        print("error: image not found!")
        exit()


    img = cv2.resize(img, size, interpolation= cv2.INTER_LINEAR) #resize image
    x = size[0] #image width
    y = size[1] #image height
    

    characters = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."] #characters from dark to light

    file = open(output_file_name, "w") #open/create txt file

    luku = 255 // len(characters) #calculates the number of different darkness areas from the number of characters in use

    for i in range(y):
        for j in range(x):

            if j != x -1:
                if img[i][j] // luku -1 >= 0: #examine the brightness of the spot
                    file.write(f"{characters[(img[i][j] // luku) -1]}") #calculates which character to take from the list and writes it to a file.
                else: 
                    file.write(f"{characters[0]}")
                
                    
            else: #newline
                if img[i][j] // luku -1 >= 0: #examine the brightness of the spot
                    file.write(characters[(img[i][j] // luku) -1] + "\n") #calculates which character to take from the list and writes it to a file.
                else: 
                    file.write(characters[0] + "\n")

    file.close() #close file







def PrintHelp():
    

    print("argv 1     image file name or path")
    print("argv 2     output file name, default same as image file name")
    print("argv 3     resize image, default = 200x200")
    print("\n")    
    print("example: 'image1.png textimage.txt 100x100'")
    print("\n")
    
    print("options: ")
    print("-h     show this message")
    
    




if __name__ == "__main__": #global scope

    #read command line arguments:
    
    if len(sys.argv) < 2: #no arguments given
        PrintHelp()
        exit() 

    if sys.argv[1] in ["-help","help","-h"]:
        PrintHelp()
        exit()


    image_path = sys.argv[1] 
    output_file_name = sys.argv[1] + ".txt" #default output file name
    new_resolution = (200,200) #default resolution


    if len(sys.argv) == 2: #only image file path given
        image_path = sys.argv[1]

    elif len(sys.argv) == 3: #image file path and output file name is given
        image_path = sys.argv[1]
        output_file_name = sys.argv[2]

    elif len(sys.argv) == 4: #image file path, output file name,resolution given

        image_path = sys.argv[1]
        output_file_name = sys.argv[2]

        try:
            new_resolution = sys.argv[3].split("x")
            new_resolution[0] = int(new_resolution[0]) #str to int
            new_resolution[1] = int(new_resolution[1])
        except:
            print("error: invalid resolution argument")
            exit()




    ImageToAscii(image_path,new_resolution,output_file_name) #convert an image to asci and write it to a file




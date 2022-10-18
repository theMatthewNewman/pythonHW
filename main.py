import mazeSolver
import txtParser

def main():
    # ease of use interactive inputs
    inputfile = input("Enter input file: ")
    displayMaze = input("Display the maze?[y/n] ")
    outputFile = input("file to output: ")

    # convert the input file and output the solved maze
    txtParser.convert(inputfile,'tmp.csv')
    if displayMaze=="y":
        mazeSolver.mazeSolver("tmp.csv",True,outputFile)
    if displayMaze=="n":
        mazeSolver.mazeSolver("tmp.csv",False,outputFile)

if __name__ == "__main__":
    main()
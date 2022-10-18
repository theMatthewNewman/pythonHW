import mazeSolver
import txtParser

def main():
    inputfile = input("Enter input file: ")
    displayMaze = input("Display the maze?[y/n] ")
    outputFile = input("file to output: ")
    txtParser.Micromouse(inputfile,'tmp.csv', (1,1))
    if displayMaze=="y":
        mazeSolver.mazeSolver("tmp.csv",True,outputFile)
    if displayMaze=="n":
        mazeSolver.mazeSolver("tmp.csv",False,outputFile)

if __name__ == "__main__":
    main()
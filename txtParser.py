import shlex
import re
import csv
from pyamaze import maze,COLOR,agent
 

class convert:

    def __init__(self, infile, outfile):
        # Variable Initialization and Functions too
        self.outfile=outfile
        self.file = open(infile, 'r')
        self.lines = self.file.readlines()
        self.parsedLines = []
        self.cols = 0
        self.rows = 0
        self.parse_func()
        self.get_dimensions()
        self.maze = maze(self.rows, self.cols)
        # read the input file and get tokenizer for dictionary list
        self.arr = [[[0 for x in range(4)] for y in range(self.cols)] for z in range(self.rows)]
        self.compute_arr()
        self.write_csv()
        # process the dictionary list and sort the dictionary list
        # before write the list into a cvs file (self.csvfile)
    # this function will take an input line and parse into 5 fields
    # field 1: cell., field 2: north distance...

    def parse_func(self):

        for line in self.lines:
            temp = line.replace('"', '').replace(')', '').replace('(', '').replace(',',' ')
            temp = temp.split()
            self.parsedLines.append(temp)
        return

    # Collecting number of columns and rows

    def get_dimensions(self):
        for line in self.parsedLines:
            if int(line[0]) > self.rows:
                self.rows = int(line[0])
            if int(line[1]) > self.cols:
                self.cols = int(line[1])
        return

    # Computing and organizing array
    def compute_arr(self):
        for line in self.parsedLines:
            row = int(line[0])-1
            col = int(line[1])-1
            for i in range (2,6):
                if float(line[i]) > 0.25:
                    line[i] = 1
                else:
                    line[i] = 0

            self.arr[row][col] = line[2:]

#Writing to new csv with proper formatting for loading into pyamaze maze generation
    def write_csv(self):
        output = open(self.outfile, "w")
        output.write("cell,E,W,N,S")
        for j in range(self.cols):
            for i in range(self.rows):
                # Writing data in proper formatting
                output.write('\n"({}, {})",{},{},{},{}'.format((i+1),(j+1),self.arr[i][j][0],self.arr[i][j][1],self.arr[i][j][2],self.arr[i][j][3]))        

    def createMaze(self):
        # maze created based the self.csvfile
        self.maze.CreateMaze( loadMaze=self.outfile)
        # displace the maze based the created maze
        self.maze.run()
 

if __name__=="__main__":
    a = convert('inputfile3.txt','tmp.csv')
    a.createMaze()
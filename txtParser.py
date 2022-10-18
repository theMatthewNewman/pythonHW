from pyamaze import maze
 

class convert:

    def __init__(self, infile, outfile):
        self.file = open(infile, 'r')
        lines = self.parse_func(self.file.readlines())
        dims = self.get_dimensions(lines)
        arr = self.compute_arr(lines, dims)
        self.write_csv(arr, dims, outfile)

    def parse_func(self,lines):
        parsedLines = []
        for line in lines:
            temp = line.replace('"', '').replace(')', '').replace('(', '').replace(',',' ')
            temp = temp.split()
            parsedLines.append(temp)
        return parsedLines

    def get_dimensions(self, lines):
        rows=0
        cols=0
        for line in lines:
            if int(line[0]) > rows:
                rows = int(line[0])
            if int(line[1]) > cols:
                cols = int(line[1])
        return (rows,cols)

    def compute_arr(self,lines, dim):
        arr = [[[0 for x in range(4)] for y in range(dim[0])] for z in range(dim[1])]
        for line in lines:
            row = int(line[0])-1
            col = int(line[1])-1
            for i in range (2,6):
                if float(line[i]) > 0.25:
                    line[i] = 1
                else:
                    line[i] = 0
            arr[row][col] = line[2:]
        return(arr)

    def write_csv(self, dic, dim, outfile):
        output = open(outfile, "w")
        output.write("cell,E,W,N,S")
        for j in range(dim[1]):
            for i in range(dim[0]):
                output.write('\n"({}, {})",{},{},{},{}'.format((i+1),(j+1),dic[i][j][0],dic[i][j][1],dic[i][j][2],dic[i][j][3]))

if __name__=="__main__":
    a = convert('inputfile3.txt','tmp.csv')
    m = maze()
    m.CreateMaze(loadMaze='tmp.csv')
    m.run()
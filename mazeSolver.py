from pyamaze import maze, agent
import aStar

class mazeSolver:
    def __init__(self, maz, gui=False, output='none'):
        self.gui = gui
        self.maz = maz
        self.output=output

    def createMaze(self):
        m = maze()
        m.CreateMaze(loadMaze=self.maz)
        
        return(m)
    
    # the main function this writes a output file to the specified location
    def solveMaze(self):
        m = self.createMaze()
        path = aStar.aStar(m)
        print(path)
        if self.output != "none":
            with open(self.output, "a") as o:
                o.write(str(path))
        a=agent(m,footprints=True)
        m.tracePath({a:path})
        if self.gui: # if there is a graphical display of the maze
            m.run()
        return path

if __name__ == "__main__":
    mazeSolver("./tmp.csv",True,"solved.txt").solveMaze()
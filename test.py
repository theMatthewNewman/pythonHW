from pyamaze import maze, agent
import aStar

class mazeSolver:
    def __init__(self, maz, gui):
        self.gui = gui
        self.maz = maz

    def createMaze(self):
        m = maze()
        m.CreateMaze(loadMaze=self.maz)
        
        return(m)
    
    def solveMaze(self):
        m = self.createMaze()
        path = aStar.aStar(m)
        print(path)
        with open("mazePath.txt", "a") as o:
            o.write(str(path))
        a=agent(m,footprints=True)
        m.tracePath({a:path})
        if self.gui:
            m.run()

if __name__ == "__main__":
    mazeSolver("./maze--2022-10-11--16-50-26.csv",True).solveMaze()
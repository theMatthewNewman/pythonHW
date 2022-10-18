from pyamaze import maze, agent
import aStar

class mazeSolver:
    def __init__(self, maz, gui):
        m = maze()
        m.CreateMaze(loadMaze=maz)
        self.gui = gui
        m.run()
m = maze()
m.CreateMaze(loadMaze="./maze--2022-10-11--16-50-26.csv")
print(m)

path =aStar.aStar(m)
print(path)
with open("mazePath.txt", "a") as o:
    o.write(str(path))

a=agent(m,footprints=True)
m.tracePath({a:path})

m.run()
if __name__ == "__main__":
    mazeSolver("./maze--2022-10-11--16-50-26.csv",False)
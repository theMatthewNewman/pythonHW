from pyamaze import maze, agent
import aStar


m = maze()
m.CreateMaze(loadMaze="./maze--2022-10-11--16-50-26.csv")

path =aStar.aStar(m)
print(path)
with open("mazePath.txt", "a") as o:
    o.write(str(path))

a=agent(m,footprints=True)
m.tracePath({a:path})

m.run()

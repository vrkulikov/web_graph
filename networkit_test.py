import networkit as nk
import networkx
g = nk.generators.ErdosRenyiGenerator(10000, 0.1).generate()
nk.overview(g)
G = nk.distance.Diameter(g)
G.run()
diam = G.getDiameter()
print(diam)

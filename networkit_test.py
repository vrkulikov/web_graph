import networkit as nk
g = nk.generators.ErdosRenyiGenerator(1000,0.05).generate()
nk.overview(g)
print(nk.distance.Diameter(g).getDiameter())
import networkit as nk
g = nk.generators.ErdosRenyiGenerator(1000,0.8).generate()
nk.overview(g)

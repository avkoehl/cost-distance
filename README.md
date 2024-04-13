# Cost Distance Analysis

This package implements Djikstra's algorithm to solve for the least-cost path between points on a digital elevation model raster.
Numba is used to accelerate performance.

tools:
1. find path between source cell and nearest cell in list of target cells
2. compute cost accumulation raster representing cost to get to every cell from the nearest of the source cells
3. create sourceid raster representing the nearest source cell for every cell 
4. compute HAND raster representing the elevation difference between each cell and its nearest source cell

cost surface options:
- euclidean distance
- elevation change
- cell slope in max downhill direction

walls (unpassable cells) options: 
- nodata cells
- slope threshold
- enforce downhill path


modules:
`numba_djikstra.py` -- core algorithms  
`path.py` -- least cost path  
`accumulation.py` -- cost accumulation raster  
`hand.py` -- HAND  

# Development

1. Set local python using pyenv 
2. Run poetry install
3. Run commands through the created poetry virtual environment with `poetry run`

to add jupyter kernel:
```
poetry run python -m ipykernel install --user --name cost_distance
```

# Maximize Correlation Difference

It tries to find the classes of cell-lines so that the correlation difference between two classes is maximized.

## Usage

preprocess initial data
* python init.py

### next idea

we can rank the importance of genes. Find edges whose difference between sick and normal is more than 0.5 . Insert these edges into the graph. High degree nodes are important genes.
# 1D Number Array Clustering

Don't use multidimensional clustering algorithms for a one-dimensional problem. A single dimension is much more special than you naively think, because you can actually sort it, which makes things a lot easier.

In fact, it is usually not even called clustering, but e.g. segmentation or natural breaks optimization.

You might want to look at [Jenks Natural Breaks Optimization](https://en.wikipedia.org/wiki/Jenks_natural_breaks_optimization) and similar statistical methods. [Kernel Density Estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation) is also a good method to look at, with a strong statistical background. Local minima in density are be good places to split the data into clusters, with statistical reasons to do so. KDE is maybe the most sound method for clustering 1-dimensional data.

With KDE, it again becomes obvious that 1-dimensional data is much more well behaved. In 1D, you have local minima; but in 2D you may have saddle points and such "maybe" splitting points. See this [Wikipedia illustration of a saddle point](http://en.wikipedia.org/wiki/File:Saddle_pt.jpg), as how such a point may or may not be appropriate for splitting clusters.

See [this answer](https://stackoverflow.com/a/35151947/1060350) for an example how to do this in Python (green markers are the cluster modes; red markers a points where the data is cut; the y axis is a log-likelihood of the density):

## References
1. Allan Grønlund, Kasper Green Larsen, Alexander Mathiasen, Jesper Sindahl Nielsen:
Fast Exact k-Means, k-Medians and Bregman Divergence Clustering in 1D.
https://arxiv.org/pdf/1701.07204.pdf
1. Wang H, Song M. Ckmeans.1d.dp: Optimal k-means Clustering in One Dimension by Dynamic Programming. R J. 2011 Dec;3(2):29-33. PMID: 27942416; PMCID: PMC5148156.
1. Anony Mousse, 1D Number Array Clustering, Stackoverflow, https://stackoverflow.com/questions/11513484/1d-number-array-clustering
1.  Chris Moffitt, Finding Natural Breaks in Data with the Fisher-Jenks Algorithm, https://pbpython.com/natural-breaks.html
2. Fast Fisher-Jenks breaks for Python, https://github.com/mthh/jenkspy

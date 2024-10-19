import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage
import matplotlib.colors as mcolors

def plot_distance_map(norm_counts_file):
    norm_counts_df = pd.read_csv(norm_counts_file, index_col=0)
    sample_dists = pdist(norm_counts_df.T, metric="euclidean")
    sample_dist_matrix = squareform(sample_dists)

    rownames = [f"{type_}" for type_ in norm_counts_df.columns] 
    dist_df = pd.DataFrame(sample_dist_matrix, index=rownames, columns=rownames)

    linkage_matrix = linkage(sample_dists, method='average')

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_blues", ["darkblue", "white"])

    sns.set(style="white")
    sns.clustermap(dist_df, row_linkage=linkage_matrix, col_linkage=linkage_matrix,
                   cmap=cmap, figsize=(10, 10), metric="euclidean")

    plt.savefig("dist")
    print(f"Dist plot saved as dist.png")

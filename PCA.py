import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_pca(norm_counts_file):
    norm_counts_df = pd.read_csv(norm_counts_file, index_col=0)
    norm_counts_transposed = norm_counts_df.T

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(norm_counts_transposed)

    pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'], index=norm_counts_transposed.index)

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df)

    for i, sample in enumerate(pca_df.index):
        plt.annotate(sample, (pca_df.iloc[i]['PC1'], pca_df.iloc[i]['PC2']), 
                     textcoords="offset points", xytext=(5,5), ha='center', fontsize=9)

    plt.title('PCA of Normalized Expression Data')
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0] * 100:.2f}%)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1] * 100:.2f}%)')
    plt.savefig("PCA")
    print(f"Dist plot saved as PCA.png")

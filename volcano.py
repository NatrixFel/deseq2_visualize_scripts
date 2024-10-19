import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process_data(results_file):
    
    results_df = pd.read_csv(results_file)
    results_df_proc = results_df.rename(columns={'Unnamed: 0': 'target_id'})
    results_df_proc['target_id'] = results_df_proc['target_id'].astype(str)
    
    return results_df_proc

def filter_data(df):
    filtered_df = df.dropna(subset=['padj', 'log2FoldChange'])

    filtered_df.loc[:, 'pvalue'] = pd.to_numeric(filtered_df['pvalue'], errors='coerce')
    filtered_df.loc[:, 'log2FoldChange'] = pd.to_numeric(filtered_df['log2FoldChange'], errors='coerce')
    filtered_df = filtered_df.dropna(subset=['pvalue', 'log2FoldChange'])
    filtered_df['-log10(pvalue)'] = -np.log10(filtered_df['pvalue'])

    return filtered_df

def plot_volcano(df, significance_threshold, fold_change_threshold):
    df['significant'] = (df['padj'] < significance_threshold) & \
                        (np.abs(df['log2FoldChange']) > fold_change_threshold)

    df['color'] = np.where((df['log2FoldChange'] > 0) & df['significant'], 'red',
                           np.where((df['log2FoldChange'] < 0) & df['significant'], 'blue', 'grey'))

    total_points = len(df)
    significant_points = df['significant'].sum()
    significant_pos_points = ((df['log2FoldChange'] > 0) & df['significant']).sum()
    significant_neg_points = ((df['log2FoldChange'] < 0) & df['significant']).sum()
  
    plt.figure(figsize=(12, 12))
    sns.scatterplot(x='log2FoldChange', y='-log10(pvalue)', hue='color', 
                    data=df, edgecolor='none', palette={'red': 'red', 'blue': 'blue', 'grey': 'grey'}, legend=False)

    plt.axhline(y=-np.log10(significance_threshold), color='black', linestyle='--', linewidth=0.7, 
            label=f'p ⩽ {significance_threshold}\n|Log2(FC)| ⩾ {fold_change_threshold}')
    plt.axvline(x=-fold_change_threshold, color='black', linestyle='--')
    plt.axvline(x=fold_change_threshold, color='black', linestyle='--')

    plt.legend(loc="upper right", prop={'size': 14, 'weight': 'bold'})

    textstr = '\n'.join((
        f'Total points: {total_points}',
        f'Significant points: {significant_points}',
        f'',
        f'Up-regulated: {significant_pos_points}',
        f'Down-regulated: {significant_neg_points}'
    ))

    plt.gca().text(0.05, 0.95, textstr, transform=plt.gca().transAxes, 
                   fontsize=14, fontweight='bold', verticalalignment='top',
                   bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    plt.xlabel('Log2 Fold Change', fontsize=18, fontweight='bold')
    plt.ylabel('-Log10(p-value)', fontsize=18, fontweight='bold')
  
    max_y_value = df['-log10(pvalue)'].max() + 10 
    min_x_value = min(df['log2FoldChange'].min() - 0.5, -20)
    max_x_value = df['log2FoldChange'].max() + 0.5

    plt.ylim(0, max_y_value)
    plt.xlim(min_x_value, max_x_value)

    plt.savefig("volcano")
    print(f"Volcano plot saved as volcano.png")


def run_volcano(results_file, significance_threshold, fold_change_threshold):
    merged_df = load_and_process_data(results_file)
    filtered_df = filter_data(merged_df)

    plot_volcano(filtered_df, significance_threshold, fold_change_threshold)

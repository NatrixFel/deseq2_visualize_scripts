import argparse
import pandas as pd
import volcano  
import dist_plot
import pca

def main():
    parser = argparse.ArgumentParser(description="Analyze DESeq2 results and generate plots.")
    parser.add_argument("--dds", help="Path to the DESeq2 results CSV file.")
    parser.add_argument("--norm_file", help="Path to the DESeq2 normalization CSV file")
    
    parser.add_argument("--sign", default=0.05, type=float, help="Significance threshold for volcano plot.")
    parser.add_argument("--fc", default=2, type=float, help="Fold change threshold for volcano plot.")
    
    parser.add_argument("--volcano", action="store_true", help="Generate volcano plot.")
    parser.add_argument("--dist", action="store_true", help="Generate distance map.")
    parser.add_argument("--pca", action="store_true", help="Generate PCA plot.")
    

    args = parser.parse_args()

    if args.volcano:
        volcano.run_volcano(args.dds, args.sign, args.fc)

    if args.dist:
        dist_plot.plot_distance_map(args.norm_file)
    
    if args.pca:
        pca.plot_pca(args.norm_file)

if __name__ == "__main__":
    main()

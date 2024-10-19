# Make DEG visualization quite simple

``simple_DEG.py`` is a main script for make three possible pictures: PCA, distance and volcano plots.

    usage: simple_DEG.py [-h] [--dds DDS] [--annot ANNOT] [--norm_file NORM_FILE] [--sign SIGN] [--fc FC] [--volcano] [--dist] [--pca]

    Analyze DESeq2 results and generate plots.

    options:
      -h, --help            show this help message and exit
      --dds DDS             Path to the DESeq2 results CSV file.
      --annot ANNOT         Path to the BLAST annotation CSV file.
      --norm_file NORM_FILE Path to the vst or rlog normalization CSV file.
                        Path to the DESeq2 normalization CSV file.
      --sign SIGN           p-adjusted significance threshold for volcano plot (default = 0.05).
      --fc FC               Log2(Fold change) threshold for volcano plot (default = 2).
      --volcano             Generate volcano plot.
      --dist                Generate distance map.
      --pca                 Generate PCA plot.
# Examples

## Volcano plot
    usage: simple_DEG.py [-h] [--dds DDS] [--annot ANNOT] [--sign SIGN] [--fc FC] [--volcano]
![volcano](https://github.com/user-attachments/assets/c6b4d9ef-c221-4f0b-b90a-bfa3baa63c4a)

## Distance map
    usage: simple_DEG.py [-h] [--norm_file NORM_FILE] [--dist]
![dist](https://github.com/user-attachments/assets/ac351d24-12dd-417e-b39e-66ab9764552d)
    
## PCA plot
    usage: simple_DEG.py [-h] [--norm_file NORM_FILE] [--pca]
![PCA](https://github.com/user-attachments/assets/a66c1193-cd9a-49ae-bf9e-a925a9d47f2b)

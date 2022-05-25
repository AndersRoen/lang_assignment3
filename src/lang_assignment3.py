from pathlib import Path
import argparse
import os
import pandas as pd
import pandas as pd
from collections import Counter
from itertools import combinations
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)

# loading in a single file
def load_file(filename):
    filepath = os.path.join("..", "..", "..", "CDS-LANG", "network_data", filename)
    file = pd.read_csv(filepath, header=0, sep="\t")
    return file

# loading in a directory
def load_directory(directory_path):
    files = []
    with os.scandir(f"{directory_path}") as it:
        for entry in it:
            dataframes = pd.read_csv(entry, header=0, sep = "\t")
            files.append(dataframes)
    return files

# creating the network
def create_network_text(file, i):
    G = nx.from_pandas_edgelist(file, "Source", "Target", edge_attr=["Weight"])
    # visualising the network and saving it as a png
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
    outpath_viz = os.path.join("out", "visualisations", f"network{str(i)}.png")
    plt.savefig(outpath_viz, dpi=300, bbox_inches="tight")
    # as we need to plot multiple networks, we clear the plt memory every time
    plt.clf()
    return G

# creating a ticker, that helps enumerate files
def ticker():
    j = 0
    i = 0
    return j, i

# gettomg cemtrality measures
def centrality_measures(G):
    gathered = list(G.degree)
    name, degree = zip(*gathered)
    #eigenvector
    ev = nx.eigenvector_centrality(G)
    eigenvector_df = pd.DataFrame(ev.items(), columns = ["Name", "Eigenvector"])
    # betweenness 
    bc = nx. betweenness_centrality(G)
    betweenness_df = pd.DataFrame(bc.items(), columns = ["Name", "Centrality"])
    return name, degree, eigenvector_df, betweenness_df

# making the networks into pandas dataframes, and saving them as csvs
def network_dframe(name, degree, betweenness_df, eigenvector_df, i):
    list_of_columns = list(zip(name, degree, betweenness_df["Centrality"], eigenvector_df["Eigenvector"]))
    network_df = pd.DataFrame(list_of_columns, columns = ["Name", "Degree", "Betweenness Centrality", "Eigenvector Centrality"])
    root = "out/csvs"
    network_df.to_csv(os.path.join(root, f"network_analysis{str(i)}.csv"))
    return network_df

def parse_args():
    #initializing parse_args
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--filename", required = False, help = "Filename of the file you want to do network analysis on")
    ap.add_argument("-d", "--directory_path", required = False, help = "Directory of the files you want to do network analysis on")
    args = vars(ap.parse_args())
    return args

def main():
    args = parse_args()
    j, i = ticker()
    # if command line argument -f was used, do this:
    if args["filename"] is not None and args["filename"].endswith(".csv"):
        file = load_file(args["filename"])
        G = create_network_text(file, i)
        name, degree, eigenvector_df, betweenness_df = centrality_measures(G)
        network_df = network_dframe(name, degree, betweenness_df, eigenvector_df, i)
    # if command line argument -d was used, do this:
    elif args["directory_path"] is not None:
        files = load_directory(args["directory_path"])
        j, i = ticker()
        for  i, file in enumerate(files):
            print(file)
            G = create_network_text(file, i)
            name, degree, eigenvector_df, betweenness_df = centrality_measures(G)
            network_df = network_dframe(name, degree, betweenness_df, eigenvector_df, i)

if __name__ == "__main__":
    main()
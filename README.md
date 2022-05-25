# lang_assignment3

github repo link: https://github.com/AndersRoen/lang_assignment3.git

## language analytics assignment 3 description
Assignment 3 - Network analysis

In the last few classes, we've seen lots of different ways to extract quantatitive information from text data. This includes things like: distribution of grammatical features; sentiment scores; named entities; collocations; and so on. Last week, we also saw how we can use network analysis as a formalism which allows us to describe objects by their relations.

In this assignment, you are going to write a .py script which can be used for network analysis. As we saw last week, pretty much anything can be formalised as a network. We're not going to focus on creating the edgelists for this project; instead, the goal is to have a script that would work the same way on any input data, as long as the input format is correct.

So, as test data, I recommend that you use the files in the folder called network_data. However, the final script should be able to be resused and work on any undirected, weighted edgelist with the same column names.

Your script should do the following:

    If the user enters a single filename as an argument on the command line:
        Load that edgelist
        Perform network analysis using networkx
        Save a simple visualisation
        Save a CSV which shows the following for every node:
            name; degree; betweenness centrality; eigenvector_centrality
    If the user enters a directory name as an argument on the command line:
        Do all of the above steps for every edgelist in the directory
        Save a separate visualisation and CSV for each file

## Methods
This script performs network analysis on either a single file or a whole directory, depending on what input you feed it. For this assignment we worked with premade edgelists, so the script isn't equipped to handle the creation of edgelists.
The script then takes the edgelists, performs network analysis with ```networkx```. Then, it plots the network and saves it to the ```out/visualisations``` folder in png format. Then, it extracts centrality measures, namely eigenvector and betweenness centrality, makes a ```pandas dataframe``` and saves the output to the ```out/csvs``` folder

## Usage
First, you should put the files from the ```network_data``` dataset in the ```in``` folder.
To run this script, you need to run the ```setup_lang.sh``` . Then, point the command line to the ```lang_assignment3``` folder and run the ```lang_assignment.py``` script from the ```src``` folder. You need to include one of these command line arguments: ```-f``` if you want to work with a single file. This argument lets you specify the name of the file you want to perform network analysis on. If you want the script to perform network analysis on the entire directory, use the ```-d``` to specify the directory path.

## Results
The script generally works fine, the only thing I would have liked to change about it, was the fact that the output names does not transparently reflect which file belongs to which outfile. Otherwise, it provides fairly neat csv's and plots.

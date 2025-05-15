# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
        ----------
        datafile_name: str
            path to data file

        K: int
            number of clusters to use
        
        feature_names: list
            list of feature names

        Returns
        ---------
        fig: matplotlib.figure.Figure
            the figure object for the plot
        
        axs: matplotlib.axes.Axes
            the axes object for the plot
    """
   # ====> insert your code below here
    # get the data from file into a numpy array


    # create a K-Means cluster model with  the specified number of clusters

    # create a canvas(fig) and axes to hold your visualisation

    # make the visualisation
    # remember to put your user name into the title as specified


    # save it to file as specified

    data = np.genfromtxt(datafile_name, delimiter=',')

    # KMeans clustering
    model = KMeans(n_clusters=K, random_state=0)
    labels = model.fit_predict(data)

    # Create figure and axes
    fig, axs = plt.subplots(len(feature_names), len(feature_names), figsize=(12,12))

    # Colors list
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

    for i in range(len(feature_names)):
        for j in range(len(feature_names)):
            ax = axs[i, j]
            if i == j:
                for cluster_idx in range(K):
                    cluster_data = data[labels == cluster_idx, i]
                    ax.hist(cluster_data, color=colors[cluster_idx % len(colors)], alpha=0.7)
            else:
                scatter = ax.scatter(
                    data[:, j], data[:, i],
                    c=labels,
                    cmap='tab10',
                    s=10,
                    alpha=0.8
                )
    
            if i == len(feature_names) - 1:
                ax.set_xlabel(feature_names[j])
            if j == 0:
                ax.set_ylabel(feature_names[i])


    # Title
    fig.suptitle(f"Visualisation of {K} clusters by g4-adhikari", fontsize=16)

    # Save file
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig('myVisualisation.jpg')

    # if you don't delete the line below there will be problem!
    # raise NotImplementedError("Complete the function")
    
    return fig,axs

    # if you don't delete the line below there will be problem!
    raise NotImplementedError("Complete the function")
    
    return fig,ax
    
    # <==== insert your code above here

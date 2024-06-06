# use knn algorithm from scikit learn
# give a custom distance function 
#

from sklearn.neighbors import KDTree
import numpy as np

class Schedule_Finder:
    def __init__(self, majors):
        self.trees = {} #holds the trees for different majors
        self.majors = majors

    #custom distance function between two points
    def distance(x, y):
        #this is distance within one major
        #[majors (if more than one, otherwise 00), term, minors, ]
        return x-y
    
    # vectorize everything in the database
    def vectorize(self):
        return

    def build_trees(self, arr):     
        kd_tree = KDTree(arr, metric=self.distance)
        nearest_neighbor = []
        return nearest_neighbor
    

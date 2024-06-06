# use knn algorithm from scikit learn
# give a custom distance function 
#

from sklearn.neighbors import KDTree
import numpy as np
from .models import Schedule

class Schedule_Finder:
    def __init__(self, majors):
        self.trees = {} #holds the trees for different majors
        self.majors = majors

        # self.build_trees()

    #custom distance function between two points
    def distance(x, y):
        #this is distance within one major. Everything is already numbers
        # [major, minor, term, career, special things (entrepreneurship, phd), summer, concentration (specific)]

        #[major, minor, concentration, term, career, special, summer, something specific you want to learn]
        weights = [3, 7, 3, 7, 2, 2, 1, 2]
        distance = 0

        for i in range(len(x)):
            if i == 3: #if it is the term 
                distance += weights[i] * abs(x[i] - y[i])
            else:
                if x[i] != y[i]: 
                    distance += weights[i]

        return distance 
    
    def build_trees(self):    
        for major in self.majors:
            #get schedules 
            schedules = Schedule.objects.filter(major__contains=major)

            kd_tree = KDTree(schedules, metric=self.distance)
            
            #add tree to trees dict
            self.trees[major] = kd_tree
    
    def getNearestNeighbors(self, num_neighbors, major, query_schedule):
        distances, indices = self.trees[major].query([query_schedule], k=num_neighbors)
        return indices, distances
class TVSeries:
    def __init__(self, name):
        self.name = name
        self.ratings = []
    
    def __str__(self):
        return self.name + "-> avg rating:" + str(self.averageRating())
    
    def __repr__(self):
        res = self.name + " -> "
        if len(self.ratings) == 0:
            res += "no rating yet!"
        else:
            res += "ratings: "
            for elem in self.ratings:
                res += str(elem) + "-"
            res = res[:-1]
        return res
    
    def averageRating(self):
        if len(self.ratings) == 0:
            return 0
        return sum(self.ratings)/len(self.ratings)
    
    def addRating(self, rating):
        self.ratings.append(rating)
    
    def getName(self):
        return self.name
    
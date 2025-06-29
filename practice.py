class great_grand_parent:
    def great_grand_parent(self):
        print("they contribution 12.5 %, of gene")

class grant_parent (great_grand_parent):
    def grant_parents (self):
        print("they contribution 25 %, of gene")

class parents (grant_parent):

    def parents (self):
        print("they contribution 50 %, of gene")

class child (parents):

    def child(self):
        print("this is 100%, gene product")



k1 = child()
k1.great_grand_parent()


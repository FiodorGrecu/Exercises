class py_solution:
    # def subset_helper(self,)


    def sub_sets(self, sset):
        if len(sset) == 0:
            return [[]]
        subset = self.sub_sets(sset[1:])
        return subset + [[sset[0]] + s for s in subset]

        # all_subsetts = []
        # for i in range(len(sset)):
        #     if i == 0:
        #         all_subsetts.append([])
        #     for j in range(len(sset)):
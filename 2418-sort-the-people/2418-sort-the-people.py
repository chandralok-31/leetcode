class Solution:
    def sortPeople(self, name: List[str], heights: List[int]) -> List[str]:
        height_name=dict(zip(heights,name))
        name.clear()
        for key in sorted(height_name.keys(),reverse=True):
            name.append(height_name[key])
        return name
        
        
        
        
        # height_dict = dict(zip(heights,names)) # // height_dict = {180: 'Mary', 165: 'John', 170: 'Emma'}
        # names.clear()
        # for key in sorted(height_dict.keys(),reverse=True):
        #     names.append(height_dict[key])
        # return names
        
"""
Questions

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

1 . Try to reverse a list
2.  Try to access 234 out of this list
3 . Try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list

"""

import logging as lg

class ListTask:
    
    def __init__(self,l=[]):
        self.l = l

    # 1. reversing list
    def reverse_list(self,list_to_reverse):
        try:
            lg.info(f"Reversing of list function is called with input data {list_to_reverse}")
            return list_to_reverse[::-1]
        except Exception as e:
            lg.exception(str(e))

    # 2.  Try to access 234 out of this list
    def accessing_234(self):
        try:
            lg.info(f"Trying to access 234 from list {self.l}")
            return self.l[7][0]
        except Exception as e:
            lg.exception(str(e))
        
    # 3 . Try to access 456
    def accessing_456(self):
        try:
            lg.info(f"Trying to access 456 from list {self.l}")
            return self.l[5][2]
        except Exception as e:
            lg.exception(str(e))

    # 4 . Try to extract only a list collection form list l
    def extracting_list(self,extracting_from_list):
        try:
            lg.info(f"we are trying to extrace only list from the given list {extracting_from_list}")
            for val in extracting_from_list:
                if type(val) == list:
                    yield val
        except Exception as e:
            lg.exception(str(e))

    # 5 . Try to extract "sudh"
    def accessing_sudh(self):
        try:
            lg.info(f"we are trying fetch 'sudh' from the given list")
            return self.l[-1]['key1']
        except Exception as e:
            lg.exception(str(e))

    # 6 . Try to list all the key in dict element avaible in list
    def listing_all_keys(self):
        try:
            lg.info(f"trying to list all the keys from dict in list {self.l}")
            return self.l[-1].keys()
        except Exception as e:
            lg.exception(str(e))

    # 7 . Try to extract all the value element form dict available in list
    def listing_all_values(self):
        try:
            lg.info(f"trying to get values from dict inside the given list {self.l}")
            return self.l[-1].values()
        except Exception as e:
            lg.exception(str(e))

if __name__ == "__main__":
    try:
        lg.basicConfig(filename='task_01_looger.log',level=lg.INFO,format="%(asctime)s - %(name)s - %(message)s")
        l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
        new_object = ListTask(l)
        print("reverse of list:\n",new_object.reverse_list(new_object.l))
        print("\naccessing 234:\n",new_object.accessing_234())
        print("\naccessing 456:\n",new_object.accessing_456())
        print("\nExtracting List inside list:\n",list(new_object.extracting_list(new_object.l)))
        print("\naccessing sudh:\n",new_object.accessing_sudh())
        print("\nExtracting keys:\n",new_object.listing_all_keys())
        print("\nExtracting values:\n",new_object.listing_all_values())
    except Exception as e:
        lg.exception(e.__dict__)

lg.shutdown()
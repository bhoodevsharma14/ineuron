"""
l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([223,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]

Question 1. try to extract all the list entity
Question 2. try to extract all the dict entity
Question 3. try to extract all the tuple entity
Question 4. try to extract all the numeriacl data it may be a part of dict key and values.
Question 5. try to give summation of all the numeric data
Question 6. try to filter out all the odd values out all numeric data
Question 7. try to extract "ineuron" out of this data
Question 8. try to find out a number of occurances of all the data.
Question 9. try to out number of keys in dict element
Question 10. try to filter out all the string data
Question 11. try to find out alphanum in data
Question 12. try to find out multiplication of all numberic value in the individual collection inside dataset
Question 13. try to unwrape all the collection inside collection and create a flat list
"""
import task_01
import logging as lg

class Lists:
    def extract_dict(self,from_where_to_extract=[]) -> list:
        """This method is used to extract all the dictionaries of lelvel-1 from the given list or tuple and return list containing only dict"""
        try:
            lg.info(f"Trying to get all the dictionaries from {from_where_to_extract}")
            dicts = []
            for value in from_where_to_extract:
                if type(value) == dict:
                    dicts.append(value)
            else:
                return dicts
        except Exception as e:
            lg.exception(str(e))

    def extract_tuples(self,from_where_to_extract)-> list:
        """This method is used to extract all the tuples of lelvel-1 from the given list or tuple and return list containing only tuples"""
        try:
            lg.info(f"Trying to get all the tuples from {from_where_to_extract}")
            tuples = []
            for value in from_where_to_extract:
                if type(value) == tuple:
                    tuples.append(value)
            else:
                return tuples
        except Exception as e:
            lg.exception(str(e))

    def filter_odd(self,list_to_filter):
        """This method take numerical list and filter odd values from it"""
        try:
            lg.info(f"filtering odd values from {list_to_filter}")
            result = filter(lambda value: value%2 != 0,list_to_filter)
            return list(result)
        except Exception as e:
            lg.exception(str(e))

    def sum_all(self,list_to_sumup):
        """This method take list of number and sum all of them"""
        try:
            lg.info(f"Sum all the value of {list_to_sumup}")
            return sum(list_to_sumup)
        except Exception as e:
            lg.exception(str(e))
    
    def extract_numbers(self,from_where_to_extract)-> list:
        """This method is used to extract all the Numerical values till lelvel-2 from the given list,tuple,set and dict and return list containing only numbers"""
        try:
            lg.info(f"Trying to get all the tuples from {from_where_to_extract}")
            numbers = []
            for value in from_where_to_extract:
                if type(value) == int:  # if the value is int type
                    numbers.append(value)
                elif type(value) in [list,tuple,set]:  # if the value if either list,tuple or set it will filter and give only int from these
                    res = filter(lambda input:type(input) == int,value)
                elif type(value) == dict:  # if the vale is of dict datatype then we check is key or value is int or not
                    for k,v in value.items():
                        if type(k) == int:
                            numbers.append(k)
                        if type(v) == int:
                            numbers.append(v)
                numbers.extend(list(res))
            else:
                return numbers
        except Exception as e:
            lg.exception(str(e))

    def extract_ineuron(self,extract_from):
        """This method will extract 'ineuron' from the given data"""
        try:
            lg.info(f"Extract 'ineuron' from {extract_from}")
            ineuron_list = []
            for value in extract_from:
                if type(value) == str and value=='ineuron':
                    ineuron_list.append(value)
                elif type(value) in [list,tuple,set]:
                    res = filter(lambda input:input=='ineuron',value)
                    ineuron_list.extend(list(res))
                elif type(value) == dict:
                    for key,val in value.items():
                        if key == 'ineuron':
                            ineuron_list.append(key)
                        if val == 'ineuron':
                            ineuron_list.append(val)
            else:
                return ineuron_list
        except Exception as e:
            lg.exception(str(e))
    
    def flat_data(self,data_to_be_flat):
        """This method will flat the given data till level-1 only"""
        try:
            lg.info(f"flat_data method is called with argument {data_to_be_flat}")
            flat = []
            for value in data_to_be_flat:
                if type(value) in [list,tuple,set]:
                    for val in value:
                        flat.append(val)
                elif type(value) == dict:
                    for key,val in value.items():
                        flat.append(key)
                        flat.append(val)
                else:
                    flat.append(value)
            else:
                return flat
        except Exception as e:
            lg.exception(str(e))

    def count_occurance(self,data):
        """This method will count the occurance of the values from the given data"""
        try:
            lg.info(f"Count occurance of every data in {data}")
            occurance = {}
            for val in data:
                occurance[val] = data.count(val)
            else:
                return occurance
        except Exception as e:
            lg.exception(str(e))

    def count_keys(self,data):
        """This method will count the number of keys present in dict inside data"""
        try:
            lg.info(f"Counting keys from the dict data {data}")
            count_of_keys = 0
            for value in data:
                if type(value) == dict:
                    count_of_keys += len(value)
            else:
                return count_of_keys
        except Exception as e:
            lg.exception(str(e))

    def extract_string(self,data):
        """This method will extract all the string present in the given data"""
        try:
            lg.info(f"Extracting String data from  {data}")
            strings = []
            for value in data:
                if type(value) == str:
                    strings.append(value)
                elif type(value) in [list,tuple,set]:
                    res = filter(lambda input: type(input)==str,value)
                    strings.extend(list(res))
                elif type(value) == dict:
                    for key,val in value.items():
                        if type(key) == str:
                            strings.append(key)
                        if type(val) == str:
                            strings.append(val)
            else:
                return strings
        except Exception as e:
            lg.exception(str(e))

    def extract_alphanum(self,data):
        """This method extract alphanum values from the given data"""
        try:
            lg.info(f"Extracting alphanum data from {data}")
            alphanum = filter(lambda input:input.isalnum(),data)
            return list(alphanum)
        except Exception as e:
            lg.exception(str(e))

    def product_of_numerical_data(self,data):
        """This method will return the product of all numerical data"""
        try:
            lg.info(f"Finding product of numerical data {data}")
            product = 1
            for value in data:
                product *= value
            else:
                return product
        except Exception as e:
            lg.exception(str(e))

if __name__ == '__main__':
    try:
        lg.basicConfig(filename='task_02_looger.log',level=lg.INFO,format="%(asctime)s - %(name)s - %(message)s")

        l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([223,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
        
        # Question 1
        # Extracting List form the given list
        list_task_object = task_01.ListTask()
        child_lists = list(list_task_object.extracting_list(l))
        print(f"\nQuestion 1. Extracting lists:-\n{child_lists}")
        
        # this will work only if the decorator @classmethod is used with extracting_list()
        # print(list(task_01.ListTask.extracting_list(l)))
        

        # Question 2
        lists_object = Lists()
        dictionaries = lists_object.extract_dict(l)
        print(f"\nQuestion 2. Extracting Dictionaries:-\n{dictionaries}")


        # Question 3
        print(f"\nQuestion 3. Extracting Tuple:-\n{lists_object.extract_tuples(l)}")

        # Question 4
        numbers_only = lists_object.extract_numbers(l)
        print(f"\nQuestion 4. Extracting Numerical values:-\n{numbers_only}")

        # Question 5
        print(f"\nQuestion 5. Sum all Numerical values:-\n{lists_object.sum_all(numbers_only)}")

        # Question 6
        print(f"\nQuestion 6. odd values:-\n{lists_object.filter_odd(numbers_only)}")

        # Question 7
        print(f"\nQuestion 7. extracting 'ineuron' :-\n{lists_object.extract_ineuron(l)}")

        # Question 8
        flat_data = lists_object.flat_data(l)
        print(f"\nQuestion 8. Number of Occurance of data :-\n{lists_object.count_occurance(flat_data)}")
        
        # Question 9
        print(f"\nQuestion 9. Total number of Keys in all dictionaies:-\n{lists_object.count_keys(l)}")
        
        # Question 10
        strings = lists_object.extract_string(l)
        print(f"\nQuestion 10. Extracting only string data:-\n{strings}")

        # Question 11
        print(f"\nQuestion 11. Extracting alphanum:-\n{lists_object.extract_alphanum(strings)}")

        # Question 12
        print(f"\nQuestion 12. Multiplication of Numerical data:-\n{lists_object.product_of_numerical_data(numbers_only)}")

        # Question 13
        print(f"\nQuestion 13. Flat the data:-\n{flat_data}")

    except Exception as e:
        lg.exception(str(e))

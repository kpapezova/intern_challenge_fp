import json
from statistics import mean
import pandas as pd


class Mentee:

    def __init__(self, data):
        self.data = pd.read_csv(data)
        self.num_of_mentees = len(self.data)
        self.languages = set(self.data['language'])


'''

    def prep_fullname(self, data):
        "Return a list of mentees full names"
        full_names = []

        for row in data:
            first_name = row["first_name"]
            last_name = row["last_name"]
            full_names.append(first_name + " " + last_name)

        return full_names


    def get_average(self, fullnames):
        "Return an average length of mentees full names"
        inp_lst = []
        
        for i in range(len(fullnames)):
            length = len(fullnames[i]) - fullnames[i].count(" ")
            inp_lst.append(length)

        list_avg = round(mean(inp_lst))

        return list_avg


    def get_longest(self, fullnames):
        "Return longest full name/s"
        longest_len = 0
        longest_names = [" "]

        for i in range(len(fullnames)):
            length = len(fullnames[i]) - fullnames[i].count(" ")
            if length > longest_len:
                longest_names.clear()
                longest_names.append(fullnames[i])
                longest_len = length
            elif length == longest_len:
                longest_names.append(fullnames[i])
            else:
                pass

        return longest_len, longest_names


    def get_shortest(self, fullnames):
        "Return shortest full name/s"
        shortest_len = 20
        shortest_names = [" "]

        for i in range(len(fullnames)):
            length = len(fullnames[i]) - fullnames[i].count(" ")
            if length < shortest_len:
                shortest_names.clear()
                shortest_names.append(fullnames[i])
                shortest_len = length
            elif length == shortest_len:
                shortest_names.append(fullnames[i])
            else:
                pass

        return shortest_len, shortest_names

'''
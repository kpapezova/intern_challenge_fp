import json
from statistics import mean
import pandas as pd


class Mentee:

    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.num_of_mentees = len(self.data)
        self.languages = set(self.data["language"])
        self.full_names = self.data["first_name".strip()] + ' ' + self.data["last_name".strip()]


    def get_average(self):
        """Return an average length of mentees full names"""
        inp_lst = []
        
        for i in range(len(self.full_names)):
            length = len(self.full_names[i]) - self.full_names[i].count(" ")
            inp_lst.append(length)

        list_avg = round(mean(inp_lst))

        return list_avg


    def get_longest(self):
        """Return longest full name/s"""
        longest_len = 0
        longest_names = [" "]

        for i in range(len(self.full_names)):
            length = len(self.full_names[i]) - self.full_names[i].count(" ")
            if length > longest_len:
                longest_names.clear()
                longest_names.append(self.full_names[i])
                longest_len = length
            elif length == longest_len:
                longest_names.append(self.full_names[i])
            else:
                pass

        return longest_len, longest_names


    def get_shortest(self):
        """Return shortest full name/s"""
        shortest_len = 20
        shortest_names = [" "]

        for i in range(len(self.full_names)):
            length = len(self.full_names[i]) - self.full_names[i].count(" ")
            if length < shortest_len:
                shortest_names.clear()
                shortest_names.append(self.full_names[i])
                shortest_len = length
            elif length == shortest_len:
                shortest_names.append(self.full_names[i])
            else:
                pass

        return shortest_len, shortest_names
    

if __name__ == "__main__":
    users = Mentee("mentees_list.csv")
    print(users.data)
    print(f"Number of mentees: {users.num_of_mentees}")
    print(f"Set of languages that all mentees speak {users.languages}")
    print(f"Mentees full names {users.full_names}")
    print(f"An average length of mentees full names is {users.get_average()} characters.")
    print(f"The longest full name/s: {users.get_longest()[1]} with {users.get_longest()[0]} characters.")
    print(f"The shortest full name/s: {users.get_shortest()[1]} with {users.get_shortest()[0]} characters.")
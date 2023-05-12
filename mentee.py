import json
import csv
from statistics import mean


class Mentee:

    def load_mentee(self, csv_file):
        "Load csv file and clean data (get rid of white spaces). Return list of dictionaries (one dict for each mentee)"
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)       # to make first line as variable "header"
            data = []      # list of mentees
            for row in reader:
                data.append({header[0] : int(row[0]), header[1] : row[1].strip(), header[2] : row[2].strip(), header[3] : row[3].strip()})
        
            return data


    def count_mentees(self, data):
        "Count mentees and return the number of mentees"
        num_of_mentees = len(data)
        return num_of_mentees


    def spoken_languages(self, data):
        "Return a set of languages that all mentees know"
        all_languages = set()

        for row in data:
            language = row["language"]
            all_languages.add(language)

        return all_languages


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

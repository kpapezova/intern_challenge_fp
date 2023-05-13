## name of csv file: mentees_list.csv
import mentee
import json


"""Load mentees from csv"""
csv_file = "mentees_list.csv"
users = mentee.Mentee(csv_file)
## or input the name of csv
# csv_input = input("Insert a name of csv file: ")
# users = mentee.Mentee(csv_input)


"""Get a number of all mentees"""
number_of_mentees = users.num_of_mentees


"""Set of all languages that mentees know"""
all_lang = users.languages


"""Preparation of full names"""
names = users.full_names


"""Average length of mentees full name"""
avg_length = users.get_average()


"""Longest name/s"""
longest_length, l_name = users.get_longest()


"""Shortes name/s"""
shortest_length, s_name = users.get_shortest()


"""Report"""
report_data = {"number of mentees" : number_of_mentees, "languages" : list(all_lang), "average full name length" : avg_length, "longest length full name/s" : (longest_length, l_name), "shortest length full name/s" : (shortest_length, s_name)}


with open("mentees_report.json", "w") as f:
    json.dump(report_data, f, indent=4)

print('A report named "mentees_report.json" has been created.')

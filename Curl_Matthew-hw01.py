# Matthew Curl
# UWYO COSC 1010
# 10/15/2024
# HW 01
# Lab Section: 13D
# Sources, people worked with, help given to: N/A
# your
# comments
# here

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
students = [
     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution:

#set up an empty dictionary for the scores
average_scores = {}
#get the student's scores average and name and store it in the dictionary
for student in students:
    name = student["name"]
    scores = student["scores"]
    # find average by using the sum of the values of the scores dictionary and dividing by the length function
    avg_score = sum(scores.values())/ len(scores)
    #store a new key-value in empty dictionary
    average_scores[name] = avg_score

# make a nested if statement in a for to check the average score and print it if greater than 80
for name, average_score in average_scores.items():
    if average_score > 80:
        print(f"{name} got an average score greater than 80.")
        



"""
Copyright (C) 2020-2050
    -   Marina Prieto Pech
    -   Sergio Silvestre Pavon
    -   Josue Carlos Zenteno Yave
"""
import os

class TextManager:

    ###########################---Constructor---###########################
    def __init__(self):
        pass
    ###########################---Main Methods---##########################
    @staticmethod
    def generate_txt_solution(solution, rows, columns):
        output_txt = open("solution_"+str(rows)+"_"+str(columns)+".txt", "w")
        for x in solution:
            output_txt.write(x.toString() + os.linesep)
        
        output_txt.close()
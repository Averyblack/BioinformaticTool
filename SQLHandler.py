import sqlite3
from sqlite3 import Error
import pandas as pd
import openpyxl
import random
import itertools
import re
import time

#creates the DB and inserts data into it using excel sheet
conn = sqlite3.connect('database\Enzymes.db')
cur = conn.cursor()
enzymes = pd.read_excel('enzymes2.xlsx', sheet_name='Enzymes', header=0)
enzymes.to_sql("Enzymes", conn, if_exists = "replace", index = False)

#Search through the enzyme DB and returns sequence recognized by given enzyme and exact cut location
def Quering(enzyme):
    sql_select_query = """SELECT Code FROM Enzymes WHERE Name = ?"""
    cur.execute(sql_select_query, (enzyme,))
    seq = cur.fetchone()[0]
    sql_select_query_pos = """SELECT Position FROM Enzymes Where Name = ?"""
    cur.execute(sql_select_query_pos, (enzyme,))
    pos = cur.fetchone()[0]
    sql_select_query_pos2 = """SELECT Position2 FROM Enzymes Where Name = ?"""
    cur.execute(sql_select_query_pos2, (enzyme,))
    pos2 = cur.fetchone()[0]
    return seq, pos, pos2

#Populates the drop down list with all enzymes presten in enzymes DB
def ListPopulation():
    cur.execute("SELECT Name FROM Enzymes")
    z = cur.fetchall()
    y = []
    for x in z:
        y.append(x[0])
    return y

#Generate every possible variant of the sequence with unspecified nucleotides recognised by enzyme
def optionGeneration(seq):
    M = ["A", "C"]
    R = ["A", "G"]
    Y = ["C", "T"]
    S = ["C", "G"]
    W = ["A", "T"]
    B = ["C", "G", "T"]
    D = ["A", "G", "T"]
    H = ["A", "C", "T"]
    V = ["A", "C", "G"]
    N = ["A", "C", "G", "T"]
    options = [seq]
    if "N" in seq:
        blocks = re.findall("N+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(N, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("N+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "N" in option:
            options.remove(option)

    if "M" in seq:
        blocks = re.findall("M+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(M, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("M+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "M" in option or len(option) != len(seq):
            options.remove(option)


    if "R" in seq:
        blocks = re.findall("R+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(R, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("R+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "R" in option or len(option) != len(seq):
            options.remove(option)


    if "Y" in seq:
        blocks = re.findall("Y+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(Y, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("Y+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "Y" in option or len(option) != len(seq):
            options.remove(option)

    if "S" in seq:
        blocks = re.findall("S+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(S, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("S+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "S" in option or len(option) != len(seq):
            options.remove(option)

    if "W" in seq:
        blocks = re.findall("W+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(W, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("W+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "W" in option or len(option) != len(seq):
            options.remove(option)

    if "B" in seq:
        blocks = re.findall("B+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(B, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("B+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "B" in option or len(option) != len(seq):
            options.remove(option)

    if "D" in seq:
        blocks = re.findall("D+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(D, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("D+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "D" in option or len(option) != len(seq):
            options.remove(option)

    if "H" in seq:
        blocks = re.findall("H+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(H, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("H+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "H" in option or len(option) != len(seq):
            options.remove(option)

    if "V" in seq:
        blocks = re.findall("V+", seq)
        index = 0
        for x in range(len(blocks)):
            blockLen = len(blocks[index])
            index += 1
            for option in options:
                op = itertools.product(V, repeat = blockLen)
                for opt in op:
                    opt = ''.join(opt)
                    o = re.sub("V+", opt, option, 1)
                    if o  not in options:
                        options.append(o)

    for option in options[:]:
        if "V" in option or len(option) != len(seq):
            options.remove(option)


    return options

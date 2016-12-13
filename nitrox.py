#
# Nitrox Interpreter
# Version 0.1
#
# Licensed under the MIT license
#
# Created by matthewgallant on 12/4/16
#
# (c) 2016 Matthew Gallant
#

# Imports
from sys import argv
from sys import platform
from subprocess import call
import os
import pydb

# Initialize Database
pydb.create("nitrox")

# Handle File Arguments
script, filename = argv
txt = open(filename)

# Read Text File
text = txt.read()

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mult(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

# Search Code For Commands
for line in text.splitlines():
    if line.startswith("print"):
        print_var = line[6:]
        print(print_var)

    if line.startswith("var"):
        var = line[4:]
        var_name, var_value = var.split(' = ')
        pydb.addrow("nitrox","vars",var_name,var_value)

    if line.startswith("out"):
        out = line[4:]
        var = pydb.read("nitrox","vars",out)
        print(var)

    if line.startswith("input"):
        input_var = line[6:]
        input_var_name, input_text = input_var.split(" = ")
        input_data = raw_input(input_text)
        pydb.addrow("nitrox","vars",input_var_name,input_data)

    if line.startswith("compare"):
        cmp_var = line[8:]
        cmp_name, cmp_statement = cmp_var.split(" --> ")
        cmp_var1, cmp_var2 = cmp_statement.split(" == ")
        var1 = pydb.read("nitrox","vars",cmp_var1)
        var2 = pydb.read("nitrox","vars",cmp_var2)
        if var1 == var2:
            pydb.addrow("nitrox","vars",cmp_name,"true")
        if var1 != var2:
            pydb.addrow("nitrox","vars",cmp_name,"false")

    if line.startswith("if"):
        if_var = line[3:]
        if_name, if_statement = if_var.split(" --> ")
        if_newvar, if_newvar_data = if_statement.split(" == ")
        if_name_var = pydb.read("nitrox","vars",if_name)
        if if_name_var == "true":
            pydb.addrow("nitrox","vars",if_newvar,if_newvar_data)
        if if_name_var == "false":
            pydb.addrow("nitrox","vars",if_newvar,"")

    if line.startswith("python"):
        py_cmd = line[7:]
        exec py_cmd

    if line.startswith("add"):
        add_vars = line[4:]
        add_num1, add_num2 = add_vars.split(' + ')
        add_num3 = int(add_num1)
        add_num4 = int(add_num2)
        print(add(add_num3,add_num4))

    if line.startswith("sub"):
        sub_vars = line[4:]
        sub_num1, sub_num2 = sub_vars.split(' - ')
        sub_num3 = int(sub_num1)
        sub_num4 = int(sub_num2)
        print(sub(sub_num3,sub_num4))

    if line.startswith("mult"):
        mult_vars = line[5:]
        mult_num1, mult_num2 = mult_vars.split(' * ')
        mult_num3 = int(mult_num1)
        mult_num4 = int(mult_num2)
        print(mult(mult_num3,mult_num4))

    if line.startswith("div"):
        div_vars = line[4:]
        div_num1, div_num2 = div_vars.split(' / ')
        div_num3 = int(div_num1)
        div_num4 = int(div_num2)
        print(div(div_num3,div_num4))

    if line.startswith("start"):
        file = open('nitrox/vars.db', 'w+')
        os.remove("nitrox/vars.db")
        file = open('nitrox/vars.db', 'w+')
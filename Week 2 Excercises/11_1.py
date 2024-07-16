import os

source_file_name = "motto.txt"

path1 = os.path.dirname(os.path.abspath(__file__))
try:
    source_handle = open(path1 + '/' + source_file_name, 'w')
    source_handle.write("Fiat Lux!\n")
    source_handle.write("Let there be light!")
except(SyntaxError):
    print("no")

finally:
    source_handle.close()
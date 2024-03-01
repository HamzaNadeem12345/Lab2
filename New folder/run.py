
#***************************************
#***************************************
#
# WARNING:
#    DO NOT MODIFY THIS FILE IN ANY WAY
#
#***************************************
#***************************************

import sys
from lab01 import *

argc = len(sys.argv)
if argc <= 1:
    print("Invalid arguments")
    print("usage:    python3 run F[section no]")
    print("example:  python3 run F1311")
    exit(0)
    
function = (sys.argv[1]).upper()

if function == "F1311":
    F1311()
elif function == "F1321":
    if argc != 4:
        print("ERROR: F1321 - Some arguments either are missing or extra")
        exit(0)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    print("function returned: ", F1321(a,b))
elif function == "F1322":
    F1322()
elif function == "F1341":
    F1341()
elif function == "F1411":
    if argc != 3:
        print("ERROR: F1411 - Some arguments either are missing or extra")
        exit(0)
    score = int(sys.argv[2])
    print("function returned: ", F1411(score))
elif function == "F1412":
    if argc != 3:
        print("ERROR: F1412 - Some arguments either are missing or extra")
        exit(0)
    n = int(sys.argv[2])
    F1412(n)
elif function == "F1413":
    if argc != 3:
        print("ERROR: F1413 - Some arguments either are missing or extra")
        exit(0)
    n = int(sys.argv[2])
    F1413(n)
elif function == "F1414":
    print("function returned: ", F1414())
elif function == "F1511":
    if argc != 4:
        print("ERROR: F1511 - Some arguments either are missing or extra")
        exit(0)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    print("function returned: ", F1511(a,b))

elif function == "F1512":
    if argc != 3:
        print("ERROR: F1512 - Some arguments either are missing or extra")
        exit(0)
    C = int(sys.argv[2])
    print("function returned: ", F1512(C))
elif function == "F1513":
    if argc != 3:
        print("ERROR: F1513 - Some arguments either are missing or extra")
        exit(0)
    n = int(sys.argv[2])
    print("function returned: ", F1513(n))
    
elif function == "F1514":
    if argc != 5:
        print("ERROR: F1514 - Some arguments either are missing or extra")
        exit(0)
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    c = int(sys.argv[4])
    print("function returned: ", F1514(a,b,c))
    
elif function == "F1611":
    F1611()
elif function == "F1612":
    F1612()
elif function == "F1613":
    F1613()
elif function == "F1614":
    if argc != 4:
        print("ERROR: F1614 - Some arguments either are missing or extra")
        exit(0)
    sum = float(sys.argv[2])
    avg = float(sys.argv[3])
    F1614(sum, avg)
    
elif function == "F1615":
    if argc != 3:
        print("ERROR: F1615 - Some arguments either are missing or extra")
        exit(0)
    n = int(sys.argv[2])
    print("function returned: ", F1615(n))
    
elif function == "F1621":
    F1621()
elif function == "F1622":
    print("function returned: ", F1622())
  
else:
    print("Invalid task")
    exit(0)


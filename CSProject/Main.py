import sys

from CSProject.Contract import Contract
from CSProject.stocks import printValues


class Main:
    data = printValues("GOOG")
    for c in data:
        print(c)



#!/bin/bash
import os

if __name__ == "__main__":

    os.system("rm -rf reports")
    #os.system("rmdir/s /q reports")
    os.system("mkdir reports")
    dir = os.path.dirname(os.path.abspath("__name__"))
    test_path = os.path.join(dir,"testsuites/login_suit.yml")
    print(test_path)
    os.system(f"hrun % s" % test_path)
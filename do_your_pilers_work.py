#!/usr/bin/python3
# Main script to test what pilers are installed
# Author: Alex Huft
import shutil
import subprocess


class Colors:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    reset = "\u001b[0m"


compilers = {"gcc": False,
             "g++": False,
             "python3": False,
             "javac": False,
             "go": False,
             "rustc": False,
             "node": False,
             "tsc": False,
             "lua": False,
             "ruby": False}

test_files = ["test.c", "test.cpp", "test.py", "test.java", "test.go", "test.rs", "test.js", "testts.ts", "test.lua",
              "test.rb"]


def command_exists(cmd: str) -> bool:
    if shutil.which(cmd) is not None:
        return True
    return False


if __name__ == "__main__":
    # we have to make sure make is installed
    # before we do anything else
    if command_exists("make") is None:
        print("Please install 'make' through your package manager")

    # if make is installed we can continue with the program
    # This first loop checks if the piler exists and if it
    #     does then we can set the value to True
    for piler, exists in compilers.items():
        if command_exists(piler):
            compilers[piler] = True
            print(f"{piler:<12}{Colors.green}found{Colors.reset}")
        else:
            print(f"{piler:<12}{Colors.red}not found{Colors.reset}")

    # new line
    print()

    # Now we can go over the pilers again and if it exists
    #     Then we can use the test files to check that
    #     it is working
    for piler, exists in compilers.items():
        if exists:
            p = subprocess.run(f"make {piler}", shell=True)
            if p.returncode == 0:
                print(f"{piler:<12}{Colors.green}working{Colors.reset}")
            else:
                print(f"{piler:<12}{Colors.red}not working{Colors.reset}")

    print("\nClearing test files")
    subprocess.run(f"make clean", shell=True)

#!/usr/bin/python3
# Main script to test what pilers are installed
# Author: Alex Huft
import shutil
import subprocess


compilers = ["gcc", "g++", "python3", "javac", "go", "rustc", "node", "tsc", "lua", "ruby"]
cmd_exists = [False, False, False, False, False, False, False, False, False, False]
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
    for index, compiler in enumerate(compilers):
        if command_exists(compiler):
            cmd_exists[index] = True
            print(f"{compiler:<12}found")
        else:
            print(f"{compiler:<12}not found")

    print()

    for index, value in enumerate(compilers):
        if cmd_exists[index]:
            print(f"**** testing {value} ****")
            p = subprocess.run(f"make {value}", shell=True, check=True)
            print(f"{value} works correctly")

    print("\nClearing binaries")
    subprocess.run(f"make clean", shell=True)

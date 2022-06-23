#!/usr/bin/python3
# Main script to test what compilers are installed
# Author: Alex Huft
import shutil


compilers = ["gcc", "g++", "python3", "java", "go", "rustc", "node", "tsc", "lua", "ruby"]
cmd_exists = [False, False, False, False, False, False, False, False, False, False]


def command_exists(cmd: str) -> bool:
    if shutil.which(cmd) is not None:
        return True
    return False


if __name__ == "__main__":
    for index, compiler in enumerate(compilers):
        if command_exists(compiler):
            cmd_exists[index] = True
            print(f"{compiler:<12}found")
        else:
            print(f"{compiler:<12}not found")

#!/usr/bin/python3
# Main script to test what compilers are installed
# Author: Alex Huft
import shutil


compilers = ["gcc", "g++", "java","go", "rustc", "node", "tsc"]
cmd_exists = [False, False, False, False, False, False, False]


def command_exists(cmd: str) -> bool:
    if len(shutil.which(cmd)) > 0:
        return True
    return False


if __name__ == "__main__":


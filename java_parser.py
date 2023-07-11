#!/usr/bin/env python3
import sys
from tree_sitter import Language, Parser
from generate_parser import LIB_FILE


USAGE = "USAGE:\npython3 java_pareser.py [FILE_NAME]"

def main():
    argc = len(sys.argv)

    assert argc == 2, f"Unexpected number of arguments: {argc}\n{USAGE}"

    try:
        JAVA_LANG = Language(LIB_FILE, "java")
    except Exception as e:
        print(
            f"Exception encountered while trying to load library file," 
            f"ensure that you have generate library file first (./generate_parser.py): {e}"
        )
        return

    parser = Parser()
    parser.set_language(JAVA_LANG)

    assert False, "Not implemented"

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys
from tree_sitter import Language, Parser
from generate_parser import LIB_FILE

TEST_SRC =\
bytes(
"""
package Core;

/**
 * Basic class which represents letter in alphabet.<p>
 * Set of letters is a totally ordered set.
 */
public class Letter implements Comparable<Letter> {
    protected final int value;


    /**
     * Constructs Letter from it int value.
     */
    public Letter(int value) {
        this.value = value;
    }

    /**
     * Constructs Letter from another letter,
     * take it {@code int} value.
     */
    public Letter(Letter l) {
        this.value = l.value;
    }


    /**
     * Set of all letters totally ordered as it's {@code int} values.
     */
    @Override
    public int compareTo(Letter o) {
        if (value < o.value) {
            return -10;
        } else if (value > o.value) {
            return 10;
        }

        return 0;
    }
}
""", 
encoding="utf8"
)

USAGE = "USAGE: python3 java_pareser.py [FILE_NAME]"

def main():

    argc = len(sys.argv)

    assert argc == 2, f"Unexpected number of arguments: {argc}\n{USAGE}"

    JAVA_LANG = Language(LIB_FILE, "Java")

    parser = Parser()
    parser.set_language(JAVA_LANG)

    tree = parser.parse(TEST_SRC)

    print(tree.root_node.sexp())

    assert False, "Not implemented"

    return 0

if __name__ == "__main__":
    main()
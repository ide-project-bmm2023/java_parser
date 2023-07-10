import subprocess as sp
from pathlib import Path
from tree_sitter import Language

GRAMMAR_GIT_REPO = "https://github.com/tree-sitter/tree-sitter-java.git" 
GRAMMAR_DIR_NAME = "tree-sitter-java"
LIB_FILE = Path("build/java-lang.so")


if __name__ == "__main__":
    vendor_dir = Path("./vendor")
    vendor_dir.mkdir(parents=True, exist_ok=True)

    sp.run(["git", "clone", GRAMMAR_GIT_REPO], cwd=vendor_dir)

    Language.build_library(
        LIB_FILE, 
        [vendor_dir / GRAMMAR_DIR_NAME]
    )

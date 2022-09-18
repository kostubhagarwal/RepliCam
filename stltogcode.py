import os
import sys
import subprocess as sp



def gcode_convert(filename: str, search_dir: str) -> str:
    """Takes in an stl file and turns it into a gcode file. Returns filename of created gcode file."""
    proc = sp.Popen(["/usr/bin/bash", "-c", f"slic3r {os.path.join(search_dir, filename)}"])
    proc.wait()
    return ".".join(filename.split(".")[:-1]) + ".gcode"
    

if __name__ == "__main__":
    gcode_convert("test.stl", ".")



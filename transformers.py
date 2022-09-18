import subprocess as sp
import os


def stlify(filename: str):
    """Function that takes in a LAS file and turns it into an STL file."""

def gcodeify(filename: str, UPLOAD_FOLDER: str):
    """Function that reads a STL file from disk, then saves as gcode."""
    fname = ".".join(filename.split(".")[:-1]) + ".gcode"
    sp.Popen(["/bin/bash", "-c", f"slic3r {os.path.join(UPLOAD_FOLDER, filename)}"])
    


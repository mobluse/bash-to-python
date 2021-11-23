#!/usr/bin/python3
from subprocess import check_output
import re
import os

os.system("cd")
lines = check_output(["find", ".", "-name", ".git"]).decode("utf-8").splitlines()
for i in range(len(lines)):
    lines[i] = re.sub(r"\./", "", lines[i])
    lines[i] = re.sub(r"\.git", "", lines[i])
    print(lines[i])
    os.system("cd " + lines[i] + "; git pull; cd")

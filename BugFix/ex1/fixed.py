# This bit fixes my code by setting the CWD where I expected it to be.
# VS Code sets the CWD to the project root folder by default rather than the script's location.
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
# ------------------------------------------------------------------------------------------------

file = open("data.txt", 'w')
 
file.write("100.12" + '\n')
file.write("111.23")
 
file.close()
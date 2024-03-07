# This bit fixes my code by setting the CWD where I expected it to be.
# VS Code sets the CWD to the project root folder by default rather than the script's location.
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
# ------------------------------------------------------------------------------------------------

new_member = input('Add a new member: ') + '\n'

file = open('members.txt', 'r')
members = file.readlines()
file.close()

members.append(new_member)

file = open('members.txt', 'w')
file.writelines(members)
file.close()
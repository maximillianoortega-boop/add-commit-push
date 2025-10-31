import subprocess
import sys

Message = "Update Files."

print ("Staring add-commit-push")
print ("git status")
subprocess.run(["git", "status"])

confirm = input("Do you want pain? (y/n): ")

if confirm.lower() == "y":
    print("continuing with pain...")
else:
    print("exiting pain...")
    sys.exit()


print ("git add -A")
subprocess.run(["git", "add", "-A"])

print ("git commit -m \"" + Message + "\"")
subprocess.run(["git","commit","-m", Message])

print ("git push")
subprocess.run(["git", "push"])

"""do you want pain"""
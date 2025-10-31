import subprocess
import sys

Message = "Update Files."

#check if user has a parameter of "m"
if len(sys.argv) > 1 and sys.argv[1] == "-m":
    if len(sys.argv) > 2:
        Message = sys.argv[2]
    else:
        print ("Error: No commit message after -m")
        sys.exit(1)

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
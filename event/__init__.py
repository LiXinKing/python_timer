import os
a = os.listdir("event")
for file in os.listdir("event"):
    if "__" in file or file.split(".")[1] == "pyc":
        continue
    str = "from event.%s import %s" % (file.split(".")[0], file.split(".")[0])
    exec(str, globals())

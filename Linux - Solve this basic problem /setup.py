import json
import subprocess
with open("/home/Atul/Desktop/package.json", 'r') as f:
    commands = json.load(f)
    for k, v in commands.items():
        failed = []
        for pack, ver in commands[k].items():
            package = pack + ver
            try:
                subprocess.check_output('pip install ' + package, shell = True)
            except subprocess.CalledProcessError:
                failed.append(package)
    if not failed:
        print("Success")
    else:
        print("Following package are failed: ")
        print(*failed, sep='\n')


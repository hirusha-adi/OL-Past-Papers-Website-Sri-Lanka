from sys import argv

from src.server import app


debug = False
try:
    if str(argv[1]).lower().startswith("d") or str(argv[1]).lower().startswith("t"):
        debug = True
except IndexError:
    pass

if debug:
    print("[+] Debug Mode: On")


app.run("0.0.0.0", port=3332, debug=debug)

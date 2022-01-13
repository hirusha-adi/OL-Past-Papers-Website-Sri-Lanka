from flask import Flask, render_template


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    from sys import argv

    debug = False
    try:
        if str(argv[1]).lower().startswith("d") or str(argv[1]).lower().startswith("t"):
            debug = True
    except IndexError:
        pass

    if debug:
        print("[+] Debug Mode: On")

    app.run("0.0.0.0", port=3332, debug=debug)

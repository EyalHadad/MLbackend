from flask import Flask, request
import RNA
import tempfile
from pathlib import Path
from subprocess import call
import json



app = Flask(__name__)


#@app.route('/wsl_api')
#def hi():
	#return 'hello from mrna-mirna wsl'

@app.route('/wsl_api')
def hi():
	return 'hello from mrna-mirna wsl'

@app.route('/wsl_api/duplexfold')
def duplexfold():
	string1 = request.args.get('string1')
	string2 = request.args.get('string2')
	duplex = RNA.duplexfold(string1,string2)
	return {'structure': str(duplex.structure), 'energy': str(duplex.energy), 'i': str(duplex.i), 'j': str(duplex.j)}


@app.route('/wsl_api/plfold')
def plfold():
    region_seq = request.args.get('region_seq')
    with tempfile.TemporaryDirectory() as tmpdirname:
        acc_file: Path = Path(tmpdirname) / "mrna_acc.fa"
        with open(acc_file, 'w') as f:
            f.write(region_seq.replace('-', '') + '\n')
        cmd = 'RNAplfold -W 80 -L 40 -u 10 < {}'.format(acc_file)
        status = call(cmd, cwd=Path(tmpdirname).resolve(), shell=True)
        acc_outfile: Path = Path(tmpdirname) / "plfold_lunp"
        with acc_outfile.open('r') as f:
            ACC_allstr = f.readlines()
    print(len(ACC_allstr))
    return ACC_allstr
    
    
if __name__ == '__main__':
    command = [
        "gunicorn",
        "-w", "8",
        "-b", "0.0.0.0:3031",
        "vienna_server:app"
    ]
    #subprocess.run(command)
    app.run(port=3031)

import os
import subprocess

def run_trimmomatic(reads1, reads2, outprefix, trimmo_jar, adapters, minlen=50, verbose=0, threads=1):
    cmd = ' '.join([
        'java -Xmx1000m -jar',
        trimmo_jar,
        'PE',
        '-threads', str(threads),
        reads1,
        reads2,
        outprefix + '_1.fq',
        outprefix + '.unpaired_1.fq',
        outprefix + '_2.fq',
        outprefix + '.unpaired_2.fq',
        'ILLUMINACLIP:' + os.path.abspath(adapters) + ':2:10:7:1',
        'MINLEN:' + str(minlen)
    ])

    if verbose:
        print('Run trimmomatic:', cmd)
    subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
    os.unlink(outprefix + '.unpaired_1.fq')
    os.unlink(outprefix + '.unpaired_2.fq')

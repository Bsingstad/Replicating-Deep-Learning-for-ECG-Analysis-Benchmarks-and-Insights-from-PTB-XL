from experiments.scp_experiment import SCP_Experiment
from utils import utils
# model configs
from configs.fastai_configs import *
from configs.wavelet_configs import *
from configs.your_configs import *
from configs.next_time import * 
import sys

def main(datafolder, datafolder_icbeb, outputfolder):


    models = [
        conf_tf_next_time,
        #conf_next_time_incept
        ]

    ##########################################
    # STANDARD SCP EXPERIMENTS ON PTBXL
    ##########################################

    experiments = [
        ('exp0', 'all'),
        ('exp1', 'diagnostic'),
        ('exp1.1', 'subdiagnostic'),
        ('exp1.1.1', 'superdiagnostic'),
        ('exp2', 'form'),
        ('exp3', 'rhythm')
       ]

    for name, task in experiments:
        print(name)
        print(task)
        e = SCP_Experiment(name, task, datafolder, outputfolder, models)
        e.prepare()
        e.perform()
        e.evaluate(n_bootstraping_samples=100, bootstrap_eval=True, dumped_bootstraps=False)

    # generate greate summary table
    utils.generate_ptbxl_summary_table(folder = outputfolder)

    ##########################################
    # EXPERIMENT BASED ICBEB DATA
    ##########################################

    e = SCP_Experiment('exp_ICBEB', 'all', datafolder_icbeb, outputfolder, models)
    e.prepare()
    e.perform()
    e.evaluate()

    # generate greate summary table
    utils.ICBEBE_table(folder=outputfolder)

if __name__ == "__main__":
    if not (len(sys.argv) == 4):
        raise Exception('Include the data and model folders as arguments, e.g., python reproduce_results.py ./path/to/data/ ./path/to/icbeb/ ./path/to/output/')
    else:
        main(datafolder = sys.argv[1], datafolder_icbeb = sys.argv[2], outputfolder = sys.argv[3])

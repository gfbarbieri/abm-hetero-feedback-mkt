###########################################################################
# IMPORTS
###########################################################################

from models.market import Market
from config import base_params
import shutil
import os

###########################################################################
# EXECUTE MODEL
###########################################################################

def main():
    # Initialize model with imported parameters.
    print("Initializing market.")
    model = Market(base_params)

    # Run the model.
    print("Running model.")
    results = model.run()

    # Save model results.
    print("Model complete, saving results.")

    # Save method checks listdir() instead of path. GitHub issue outstanding.
    # results.save(exp_name='firm_dynamics_ee', path=os.path.join('..','data'))

    # Use this until issue is resolved, move data manually.
    results.save(exp_name='market_dynamics', path='data')

if __name__ == '__main__':
    main()
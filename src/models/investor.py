###########################################################################
# IMPORTS
###########################################################################

from agentpy import Agent
import numpy as np

###############################################################################
# INVESTOR AGENT
###############################################################################

class Investor(Agent):
    """ 
    Represents a market agent in the model.
    
    Attributes
    ----------
    threshold : float
        Threshold for trading decision.
    strategy : int
        Trading strategy: inactive (0), buy (1), or sell (-1).
    asset_holdings : int
        Initial asset holdings.

    Notes
    -----
    The agent's threshold is initialized according to:
    \[
    \text{threshold} \sim \mathcal{U}(0, 1)
    \]
    """

    ###########################################################################
    # INITIALIZATION
    ###########################################################################

    def setup(self):
        """
        Initialize agent attributes.
        """
        self.threshold = np.random.uniform(0, 1)  # Initialize threshold uniform [0-1).
        self.strategy = 0 # Initialize strategy as inactive.
        self.asset_holdings = 100  # Initialize asset holdings unform [0, 100).

    ###########################################################################
    # MARKET FUNCTIONS
    ###########################################################################

    def trade(self):
        """
        Execute trade based on the agent's strategy.
        
        Notes
        -----
        Updates the asset holdings based on the trading strategy.
        """

        if self.strategy == 1:  # If agent is buying.
            self.asset_holdings += 1 # Increase agent's assets by 1.
        elif self.strategy == -1: # If agent is selling
            self.asset_holdings -= 1 # Increase agent's assets by 1.

    ###########################################################################
    # STRATEGY FUNCTIONS
    ###########################################################################

    def update_threshold(self):
        """
        Update the agent's threshold based on recent price changes.
        
        Notes
        -----
        The threshold is updated with a probability of `self.p.s`.
        """

        if np.random.uniform(0, 1) < self.p['s']:
            self.threshold = np.abs(self.model.price_change)  # Update based on recent price change

    def update_strategy(self):
        """
        Update the agent's trading strategy based on the market signal and threshold.
        
        Notes
        -----
        The strategy is set to buy (1) or sell (-1) if the absolute value of the market signal
        is greater than the threshold. Otherwise, the strategy is set to inactive (0).

        The strategy is updated according to:
        \[
        \text{strategy} = 
        \begin{cases} 
        1 & \text{if } |\text{signal}| > \text{threshold} \text{ and signal > 0} \\
        -1 & \text{if } |\text{signal}| > \text{threshold} \text{ and signal < 0} \\
        0 & \text{otherwise}
        \end{cases}
        \]
        """

        # Update the strategy based on the signal and the agent's threshold.
        if np.abs(self.model.signal) > self.threshold:
            self.strategy = np.sign(self.model.signal)  # Buy (1) or Sell (-1)
        else:
            self.strategy = 0  # Inactive
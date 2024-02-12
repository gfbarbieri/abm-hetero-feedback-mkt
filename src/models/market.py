from agentpy import Model, AgentList
from investor import Investor
import numpy as np

class MarketModel(Model):
    """ 
    Represents the market model containing agents and market dynamics.
    
    Attributes
    ----------
    agents : AgentList
        List of market agents.
    signal : float
        Common noise signal for the market.
    price_change : float
        Change in price.
    price : float
        Current price of the asset.
    """

    def setup(self):
        """
        Initialize model attributes and agent list.
        """

        # Create agents.
        self.agents = AgentList(self, self.p['N'], Investor)
        
        # Initialize signal.
        self.signal = 0

        # Initialize price change.
        self.price_change = 0

        # Initialize price randomly between 0 and 1.
        self.price = np.random.uniform(0, 1)

        # Randomly select a subset of agents to track.
        self.agents_to_track = np.random.choice(self.agents, size=self.p['num_track_agents'], replace=False)

    def step(self):
        """
        Execute one time step of the model.
        
        Notes
        -----
        1. Generates a common noise signal.
        2. Updates agent strategies.
        3. Executes trades.
        4. Calculates price change.
        5. Updates agent thresholds.
        6. Records data.
        """

        # Generate common signal.
        self.signal = np.random.normal(0, self.p['D'])

        # Update strategy considering signal.
        self.agents.update_strategy()

        # Execute trades
        self.agents.trade()

        # Calculate price change (to be defined)
        self.calculate_price_change()

        # Update agent thresholds
        self.agents.update_threshold()

        # Record Data, starting at t == 1.
        
        # Record agent level data.
        for a in self.agents_to_track:
            a.record(f'Asset Holdings', a.asset_holdings)

        # Record model-level data.
        self.record('Price', self.price)
        self.record('Price Change', self.price_change)
        self.record('Excess Demand', np.sum([a.strategy for a in self.agents]))
        self.record('Average Threshold', np.mean([a.threshold for a in self.agents]))
        self.record('Trading Volume', np.count_nonzero([a.strategy for a in self.agents]))

    def calculate_price_change(self):
        """
        Calculate the change in price based on excess demand and market depth.
        
        Notes
        -----
        1. Calculates excess demand.
        2. Calculates average excess demand.
        3. Calculates rate of return using the linear price impact function.
        4. Updates the price based on the rate of return.

        The rate of return and price change are calculated according to:
        \[
        r_t = \frac{Z_t}{N \lambda}
        \]
        \[
        p_t = p_{t-1} \times e^{r_t}
        \]
        """

        # Calculate excess demand
        excess_demand = np.sum([a.strategy for a in self.agents])
    
        # Calculate average excess demand
        avg_excess_demand = excess_demand / self.p['N']
    
        # Calculate rate of return using the linear price impact function
        rate_of_return = avg_excess_demand / self.p['lambda_param']

        # Update the predicted price change, which is simply the rate
        # of return.
        self.price_change = rate_of_return

        # Update the price based on the rate of return
        self.price *= np.exp(self.price_change)
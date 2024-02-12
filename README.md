## Define the Agent

#### Initialize agent parameters:
1. Threshold is set to: $\text{threshold} \sim \mathcal{U}(0, 1)$
2. Strategy is set to: 0 (inactive).
3. Holdings are set to: 100.

#### Threshold:
The threshold is updated with a probability of `s`, a parameter in the model, explained as the average update frequency. $s = 0.1$ is equivalent to 10 trading days.

#### Strategy:
The strategy is updated according to:
$$
\text{strategy} = 
\begin{cases} 
1 & \text{if } |\text{signal}| > \text{threshold} \text{ and signal > 0} \\
-1 & \text{if } |\text{signal}| > \text{threshold} \text{ and signal < 0} \\
0 & \text{otherwise}
\end{cases}
$$

## Define the Market

#### Initialize model parameters:
1. Create number of agents, N.
2. Set common signal to 0.
3. Set price change to 0.
4. Set asset price $\text{threshold} \sim \mathcal{U}(0, 1)$
5. Choose the number of agents to track.

#### Algorithm:
1. Generates a common noise signal.
2. Updates agent strategies.
3. Executes trades.
4. Calculates price change.
5. Updates agent thresholds.
6. Records data.
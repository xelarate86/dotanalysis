import data
import fetch
import neutral_probabilities
import plot

# Fetch the match IDs.
# Skip this step and use the match_ids.json below if you'd like to replicate my analysis.
fetch.match_ids()

# Fetch the match data.
fetch.matches()

# Load the match data and calculate the neutral item probabilities.
matches = data.load_matches()
neutral_probabilities.calculate(matches)

# Plot the networth.
plot.plot_networth(matches)

# Plot the gold and buyback costs.
plot.plot_gold(matches)

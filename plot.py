#!/usr/bin/env python
'''
    dota2
    -----

    Create plots for data from results file.
'''

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def buyback_cost(player):
    '''Determine the buyback cost of the player.'''
    return 100 + player['total_gold'] // 13

def plot_gold(matches):
    '''Plot the amount of gold, effective gold, and buyback cost.'''

    # Xlabel
    x = np.arange(15000)

    # Extract the players data.
    players = [j for i in matches for j in i['players']]

    # Calculate the available goid for each player.
    gold = np.array([i['gold'] for i in players])

    # Calculate the buyback cost for each player.
    buyback = np.array([buyback_cost(i) for i in players])

    # Calculate the gold - buyback cost.
    gold_minus_buyback =  gold - buyback

    # Full Trident Cost
    trident_trident_cost = np.array([6150 for i in range(len(x))])

    # Find intersections and label them.
    plt.annotate('16% of players can afford a full Trident.', xy=(2449, 6150), xytext=(2949, 15000), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('3.5% of players can afford a full Trident and Buyback.', xy=(524, 6150), xytext=(1024, 20000), arrowprops=dict(facecolor='black', shrink=0.05))

    # Plot the graph
    plt.plot(x, np.sort(trident_trident_cost)[::-1], label='Full Trident Cost')
    plt.plot(x, np.sort(gold)[::-1], label='Gold')
    plt.plot(x, np.sort(gold_minus_buyback)[::-1], label='Gold - Buyback')
    plt.legend(loc='upper right')
    plt.show()

def plot_networth(matches):
    '''Plot the amount of networth distribution.'''

    # Xlabel
    x = np.arange(15000)

    # Extract the players data.
    players = [j for i in matches for j in i['players']]

     # Calculate the networth for each player.
    networth = np.array(sorted([i['total_gold'] for i in players], reverse=True))

    # Plot the graph
    plt.plot(x, networth, label='Net Worth')
    plt.legend(loc='upper right')
    plt.show()
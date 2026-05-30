def win_rate_on(df, player, surface=None):
    """Return win rate (0.0-1.0) for a player on a surface in 2010"""

    all_players = set(df['winner_name']).union(set(df['loser_name']))
    if player not in all_players:
        raise ValueError(f"Player {player} not found in 2010 dataset")
    
    wins_mask = (df['winner_name']==player)
    losses_mask = (df['loser_name']==player)
    if surface is not None:
        wins_mask &= (df['surface']==surface)
        losses_mask &= (df['surface']==surface)

    wins = wins_mask.sum()
    losses = losses_mask.sum()
    total = wins+losses
    
    return wins/total if total>0 else 0

def head_to_head(df, player_a, player_b):
    """Return (a_wins, b_wins) - matches each player won against the other in 2010."""

    all_players = set(df['winner_name']).union(set(df['loser_name']))
    for p in (player_a, player_b):
        if p not in all_players:
            raise ValueError(f"Player {p} not found in 2010 dataset.")

    a_wins = len(df[(df['winner_name'] == player_a) & (df['loser_name'] == player_b)])
    b_wins = len(df[(df['winner_name'] == player_b) & (df['loser_name'] == player_a)])

    return (a_wins, b_wins)

def top_players_by_wins(df, n=10):
    """Return list of (player_name, wins) tuples — top N players by wins."""
    return list(df['winner_name'].value_counts().head(n).items())
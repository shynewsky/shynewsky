from collections import Counter

def solution(N, stages):
    stage_counts = Counter(stages)
    total_players = len(stages)
    failure_rates = []
    
    for i in range(1, N + 1):
        stuck_players = stage_counts.get(i, 0)
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = stuck_players / total_players
        failure_rates.append((failure_rate, i))
        total_players -= stuck_players
        
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    return [stage for rate, stage in failure_rates]

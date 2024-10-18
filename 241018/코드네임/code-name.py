class agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
agents = []
for i in range(5):
    n, s = input().split()
    agent_input = agent(n, int(s))
    agents.append(agent_input)

min_score = agents[0].score
min_idx = 0
for i in range(5):
    if agents[i].score < min_score:
        min_idx = i 
print(agents[min_idx].name, agents[min_idx].score)
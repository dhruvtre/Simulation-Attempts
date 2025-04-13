# Defining Environment
# env = 5*5

# Defining Genes
# size_gene = # Function to review existing size and determine follow on size (even or odd) and includes size math based on movement_gene_output
# movement_gene = # randomly decides one of four movement axes in each generation (top, down, left, right)

# Instantiating Agents

# agent_1 = seed size
# agent_2 = seed size

# Defining Development

# in env:
# for agent in agents_listed: 
    # agent_movement_decision = movement_gene(agent)
    # updated_agent_sizes = size_gene(agent, agent_movement_decision)
    # agent[agent_size] = updated_agent_sizes

# Running Development over Generations

# while number < number_of_generations:
# run development.py
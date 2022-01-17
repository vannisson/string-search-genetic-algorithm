import random

# Primeiro definimos a palavra/string que desejamos chegar, ou seja o modelo.
model = input("Digite a string: ")
model_size = len(model)

# Depois definimos o tamanho da população a ser gerada e quantas gerações irão existir.
population_size = 100
generations = 1500

def generate_char():
  # Retorna um elemento escolhido de forma aleatória, nesse caso utilizaremos todos os parâmetros pois buscamos valores ASCII, então definimos (inicio, parada, passo).
  return chr(random.randrange(32,126,1))

def random_population():
  # Retorna uma lista de indivíduos com a quantidade informada em "population_size".
  # A cada iteração uma string é gerada uma string com caracteres gerados de forma aleatória utilizando "generate_char()".
  # O número de iterações para forma uma string é definido por "model_size"
  population = []
  for i in range(population_size):
    dna = ""
    for j in range(model_size):
      dna += generate_char()
    population.append(dna)
  return population

def weighted_choice(items):
  # Items é uma lista de tuplas com o seguinte formato (item, peso)
  # Utilizamos o peso para determinar a probabilidade de escolher o item
  weight_total = sum((item[1] for item in items))
  n = random.uniform(0, weight_total)
  for item, weight in items:
    if n < weight:
      return item
    n = n - weight
  return item

def fitness(dna):
  # Calcula a diferença entre o caractere do individuo e do modelo (mesma posição)
  fitness = 0
  for i in range(model_size):
    if dna[i] == model[i]:
      fitness += 1
  return fitness

def mutation(dna):
  # Para cada caractere de um individuo é aplicada uma chance de mutação. Isso garante que a população não fique presa em um ótimo local.
  dna_out = ""
  mutation_chance = 0.01
  for i in range(model_size):
    if random.uniform(0,1) < mutation_chance:
      dna_out += generate_char()
    else:
      dna_out += dna[i]
  return dna_out

def crossover(dna1,dna2):
  # Realiza um cruzamento entre dois indivíduos
  # Junta partes escolhidas de forma aleatória dos dois indivíduos(pais), gerando um novo (filho)

  pos = int (random.random() * model_size)
  child = dna1[:pos] + dna2[pos:]
  return child

# Agora que temos as funções definidas, vamos gerar uma população aleatória
population = random_population()

for gen in range(generations):
  print(f"Geração: {gen} // Amostra gerada (aleatória): {population[0]}")
  
  weighted_population = []

  for individual in population:
    fit_value = fitness(individual)

    pair = (individual, fit_value)

    weighted_population.append(pair)
  
  population = []

  for i in range(int(population_size)):
    ind1 = weighted_choice(weighted_population)
    ind2 = weighted_choice(weighted_population)

    ind3 = crossover(ind1,ind2)

    population.append(mutation(ind3))

  best_string = population[0]
  max_fit = fitness(population[0])

for individual in population:
  ind_fit = fitness(individual)
  if ind_fit > max_fit:
    best_string = individual
    max_fit = ind_fit

print("A string mais compatível é: ", best_string)
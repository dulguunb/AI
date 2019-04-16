# !/usr/bin/python
import random
# an individual is better than the others if it's 
# somehow closer to the correct answer.
# fitness function tries to measure this "distance"
# between the individual and the solution.
BOARD_SIZE = 8
EVOLUTION_NUMBER = 5
def fitness(queens_locations):
    non_attacking_queen_cnt=0
    for i in range(0,BOARD_SIZE):
        row,column = queens_locations[i]
        for j in range(i+1,BOARD_SIZE):
            next_row,next_column = queens_locations[j]
            # check right diagonal
            # row+=1 column-=1 till row column == next_row , next_column
            # check left diagonal 
            tmp_row,tmp_column = row,column
            attacking_queen_found = False
            while not attacking_queen_found:
                if tmp_row == next_row and tmp_column == next_column:
                    attacking_queen_found = True
                    break
                if tmp_row > BOARD_SIZE or tmp_column < 0:
                    break
                tmp_row+=1
                tmp_column-=1
            # row-=1 column+=1 till row column == next_row , next_column
            # when it's non attacking then count
            tmp_row,tmp_column = row,column
            while not attacking_queen_found:
                if tmp_row == next_row and tmp_column == next_column:
                    attacking_queen_found = True
                    break
                if tmp_row < 0 or tmp_column > BOARD_SIZE:
                    break
                tmp_row-=1
                tmp_column+=1
            # check up
            # row+=1 column = coulmn till row column == next_row , next_column
            tmp_row,tmp_column = row,column
            while not attacking_queen_found:
                if tmp_row == next_row and tmp_column == next_column:
                    attacking_queen_found = True
                    break
                if tmp_row > BOARD_SIZE:
                    break
                tmp_row+=1
            # check down
            # row-=1 colu
            tmp_row,tmp_column = row,column
            while not attacking_queen_found:
                if tmp_row == next_row and tmp_column == next_column:
                    attacking_queen_found = True
                    break
                if tmp_row < 0:
                    break
                tmp_row-=1
            # check right 
            # row = row, column+=1
            tmp_row,tmp_column = row,column
            while not attacking_queen_found:
                if tmp_row == next_row and tmp_column == next_column:
                    attacking_queen_found = True
                    break
                if tmp_column > BOARD_SIZE:
                    break
                tmp_column+=1
            #check left 
            while not attacking_queen_found:
                if tmp_row == next_row and tmp_column == next_column:
                    attacking_queen_found = True
                    break
                if tmp_column < 0:
                    break
                tmp_column-=1
            # row = row , column-=1 till
            if not attacking_queen_found:
                non_attacking_queen_cnt+=1
        print((row,column))
    return non_attacking_queen_cnt

def selection(population):
    selected = []
    non_selected = []
    for individual in population:
        if fitness(individual) > 15:
            selected.append(individual)
        else:
            non_selected.append(individual)
    return (selected,non_selected)
def recombination(parents):
    CUT_LENGTH = 3
    for i in range(0,len(parents)-1):
        first_cut = parents[i]
        second_cut = parents[i+1]
        # this is containing a list
        first_parent = first_cut[0:CUT_LENGTH] 
        second_parent = second_cut[CUT_LENGTH:BOARD_SIZE]
        new_tail = zip(first_parent,second_parent)
        mapped = set(new_tail)
        print (new_tail)
        # [0:CUT_LENGTH]
        # [CUT_LENGTH:len(parents[i])]
        # parents[i+1][0:CUT_LENGTH] = first_cut
        # parents[i][CUT_LENGTH:len(parents[i])] = second_cut
    return parents
def produce_tuple():
    pass
def mutation(offspring):
    for i in range(0,len(offspring)):
        first_cut = offspring[i]
        random_index = random.randint(0,BOARD_SIZE-1)
        random_value = random.randint(0,BOARD_SIZE-1)
        first_cut[random_index] = random_value
    return offspring
def replacement(population,offspring):
    return 0

# termination condition: 
# (1) either goal individual appears in the population
# (2) or the overall fitness value of population is not
# being changed.
# Fitness function: number of
# nonattacking pairs of queens
# firstly an initial population is selected mostly at random.
# In every turn the population is updated with the mutated
# offspring of the individuals that are selected 
# for reproduction
def create_chess_board(n):
    # individual: a possible placement of the queens
    # where each column and each row contains exactly
    # one queen 
    board = [[0 for i in range(0,n)] for j in range(0,n)]
    return board
def select_individuals():
    queens_locations = []
    for i in range(0,BOARD_SIZE):
        random_index = random.randint(0,BOARD_SIZE-1)
        queens_locations.append((random_index,i))
    return queens_locations
def n_queen_problem():
    solved = False
    population = []
    queens_locations = select_individuals()
    for _ in range(0,EVOLUTION_NUMBER):
        population.append(select_individuals())
    
    while not solved:
        parents,_ = selection(population)
        offspring = recombination(parents)
        offspring = mutation(offspring)
        # population = replacement(population,offspring)
        if not solved: # checking the termination condition
            solved = True
    
if __name__ == '__main__':
    n_queen_problem()
# !/usr/bin/python
import random
def selection(population):
    return 0
def recombination(parents):
    return 0
def mutation(offspring):
    return 0
def replacement(population,offspring):
    return 0
# termination condition: 
# (1) either goal individual appears in the population
# (2) or the overall fitness value of population is not
# being changed.

# an individual is better than the others if it's 
# somehow closer to the correct answer.
# fitness function tries to measure this "distance"
# between the individual and the solution.

# Fitness function: number of
# nonattacking pairs of queens
def fitness(board,queens_locations):
    non_attacking_queen_cnt=0
    n = len(board)
    for i in range(0,len(board)):
        row,column = queens_locations[i]
        for j in range(i+1,len(board)):
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
                if tmp_row > n or tmp_column < 0:
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
                if tmp_row < 0 or tmp_column > n:
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
                if tmp_row > n:
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
                if tmp_column > n:
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
    for i in range(0,len(board)):
        print(board[i])
    return non_attacking_queen_cnt
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
def select_individuals(board):
    queens_locations = []
    for i in range(0,len(board)):
        random_index = random.randint(0,len(board)-1)
        board[random_index][i] = 1 
        queens_locations.append((random_index,i))
    return (board,queens_locations)
def n_queen_problem():
    solved = False
    population = []
    board = create_chess_board(8)
    board,queens_locations = select_individuals(board)
    sample = [(3,0),(2,1),(7,2),(5,3),(2,4),(4,5),(1,6),(1,7)]
    print ('sample: ' ,fitness(board,sample))
    while not solved:
        parents = selection(population)
        offspring = recombination(parents)
        offspring = mutation(offspring)
        population = replacement(population,offspring)
        if not solved: # checking the termination condition
            solved = True
    
n_queen_problem()
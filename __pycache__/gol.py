import random

def setup_game(size,max_alive):
   a_grid = get_empty_grid(size)
   fill_grid_random(a_grid,max_alive)


def get_empty_grid(size):
   new_grid = []
   for row in range(size):
       new_sublist = []
       for column in range(size):
           new_sublist.append('-')
       new_grid.append(new_sublist)
   return new_grid


def rand_alive():
   number = random.randint(1,2)
   if number == 1:
       return True
   else:
       return False



def fill_grid_random(a_grid,max_alive):
   size = len(a_grid)
   count = 0
   for r_i in range(size):
       for c_i in range(size):
            if rand_alive() == True:
               a_grid[r_i][c_i] = 'X'
               count = count + 1
               if count == max_alive:
                   return a_grid
            else:
                a_grid[r_i][c_i] = '-'
   return a_grid

rid = get_empty_grid(3)
print(fill_grid_random(grid,3))
kjh





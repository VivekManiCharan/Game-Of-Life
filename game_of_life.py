
# Initial state of cells ; '1' indicates living cell and  '0' indicates dead cell
initial_state = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]

# next_state to store the state  of cells after one second of duration
next_state = initial_state

# Priniting initial state of cells
print("Initial State")
for row in initial_state :
	print(row)

# To find the state of cells of several intervals of time
while(input("Press n to go next state ") == 'n'):
    # to find next state after one interval of time
    for row in range(0, len(initial_state)):
        for index in range(0, len(initial_state[row])) :
				
            # to count the  live cells around the present  cell
            live_cells = 0


            # counting live cells in the above row of the cell if any
            if( row - 1 >= 0):
            
                if(index-1 >= 0 and initial_state[row-1][index-1]):
                        live_cells = live_cells +1 
                if(initial_state[row-1][index]):
                        live_cells = live_cells +1 
                if(index+1 < len(initial_state[row-1]) and initial_state[row-1][index+1] ):
                        live_cells = live_cells +1 

            # counting live cells in the below row of the cell if any
            if(row+1 < len(initial_state)) :
            
                if(index-1 >= 0 and  initial_state[row+1][index-1]):
                        live_cells = live_cells +1 
                if(initial_state[row+1][index]):
                        live_cells = live_cells +1 
                if(index +1 < len(initial_state[row+1]) and initial_state[row+1][index+1] ):
                        live_cells = live_cells +1 

            # counting live cells on its left and right side if any
            if(index-1 >= 0 and initial_state[row][index-1]):
                        live_cells = live_cells +1 
            if(index+1 < len(initial_state[row]) and initial_state[row][index+1] ):
                        live_cells = live_cells +1 


            # Now we have the live cells count aroud the cell

            # if the current the cell is living cell
            if(initial_state[row][index]):

                # if the live cells are greater than 3 or less than 2 that living cell must die 
                if(live_cells < 2 or live_cells > 3):
                    next_state[row][index] = 0
            else :

                # if the dead cell has exact three number of living cells it will have life
                if(live_cells == 3):
                    next_state[row][index] = 1

    # Printing the next state 		
    print("\nNext State")
    for row in initial_state :
            print(row)

    # for next interval time , our next state will be our initial state
    initial_state = next_state






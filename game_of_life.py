
# Initial state of cells ; '1' indicates living cell and  '0' indicates dead cell
initial_state = [[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]

# next_state to store the state  of cells after one second of duration
next_state = initial_state

# Priniting initial state of cells
print("Initial State")
for row in initial_state :
	print(row)
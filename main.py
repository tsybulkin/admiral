#
#
#
import sys
import board
import rand_agent
import human_agent
from sunk_ships import ships_state

MAX_TURN = 1000


available_agents = {'random':rand_agent.RandomAgent, 'human' : human_agent.HumanAgent} #, 'dumb', 'cute'}

def run(ag1, ag2):
	if ag1 in available_agents and ag2 in available_agents:
		agent1 = available_agents[ag1]('white')
		agent2 = available_agents[ag2]('black')

		bo = board.Board(6)
		fields = bo.get_initial_ship_list('black')
		bo.fill_start_ships(agent2.set_ships(fields))
		fields = bo.get_initial_ship_list('white')
		bo.fill_start_ships(agent1.set_ships(fields))
		run_game(bo,{'white':agent1,'black':agent2})

	else:
		print 'one or both given agents are not in the list of legal agents'



def run_game(board, agents):
	grave = ships_state.copy()
	attack_state = (0,None,None)   # (Type, xy_under_attack, XYs)
	color = 'white'
	state = (color,attack_state,board,grave)
	turn = 0

	while not end_of_game(state, turn):
		action = agents[color].get_action(state)
		print turn, "color: ", color, "   action: ", action
		#board.show_board()
		if board.action_illegal(attack_state,action): board.terminate(color,grave)
		else: attack_state,grave = board.apply_action(action,attack_state,grave)
		board.show_board()
		
		color = change_color(color)
		state = (color,attack_state,board,grave)
		turn += 1

	#board.print_ships()
	print grave




def end_of_game(state, turn):
	if turn > MAX_TURN: return True
	_,_,_,grave = state
	if grave['Base']['white'] == grave['Base']['total']: return True
	if grave['Base']['black'] == grave['Base']['total']: return True
	return False



def change_color(color):
	if color == 'white': return 'black'
	elif color == 'black': return 'white'
	raise 'wrong color'




if __name__ == '__main__':
	if len(sys.argv) < 2: print "USAGE: python main.py Agent1 Agent2"
	else:
		Ag1 = sys.argv[1]
		Ag2 = sys.argv[2]

		run(Ag1, Ag2)

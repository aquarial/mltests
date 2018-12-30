import learning
import brain
import sys
import gym 




def set_space_invaders_params():
	brain.Mutation_params.input_count = 128
	brain.Mutation_params.output_count = 3
	brain.Mutation_params.upper_input_bounds = [1] * 128
	brain.Mutation_params.lower_input_bounds = [-1] * 128

def set_cart_pole_params():
	brain.Mutation_params.input_count = 4
	brain.Mutation_params.output_count = 1
	brain.Mutation_params.upper_input_bounds = [1] * 4
	brain.Mutation_params.lower_input_bounds = [-1] * 4


def set_xor_params():
	brain.Mutation_params.input_count = 2
	brain.Mutation_params.output_count = 1
	brain.Mutation_params.upper_input_bounds = [1] * 2
	brain.Mutation_params.lower_input_bounds = [-1] * 2

environments ={
'invaders':learning.evaluate_space_invaders_performance,
'cartpole':learning.evalute_pendulum_cart_performance,
'xor':learning.evaluate_xor_performance
}

environment_settings= {
'invaders':set_space_invaders_params,
'cartpole':set_cart_pole_params,
'xor':set_xor_params

}




if len(sys.argv) == 3 and sys.argv[1] == 'train':
	param_setup = environment_settings[sys.argv[2]]
	param_setup()
	result = learning.learn(environments[sys.argv[2]])

elif len(sys.argv) == 4 and sys.argv[1] == 'analyze':
	load_brain = brain.load_brain_from_file(sys.argv[3])
	param_setup = environment_settings[sys.argv[2]]
	param_setup()
	learning.visualize_performance(load_brain, environments[sys.argv[2]])
elif len(sys.argv) == 4 and sys.argv[1] == 'improve':
	load_brain = brain.load_brain_from_file(sys.argv[3])
	param_setup = environment_settings[sys.argv[2]]
	param_setup()
	result = learning.learn_from_existing(load_brain, environments[sys.argv[2]])
else:
	print('INVALID USAGE')
	

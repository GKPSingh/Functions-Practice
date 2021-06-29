# "Write a function that takes two arguments (name and phase_of_day) and return string in the format:  Good Afternoon Lauren!
# If phase_of_day is morning then return Good Morning Lauren
# If phase_of_day is evening then return Good Evening Lauren"

def name_phase(name, phase_of_day):
    if phase_of_day == 'Morning':
        print(f'Good {phase_of_day} {name}')
    elif phase_of_day == 'Evening':
        print(f'Good {phase_of_day} {name}')
    else:
        pass



name_phase('Lauren','Evening')


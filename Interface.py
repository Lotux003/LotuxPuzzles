import os, sys, time, subprocess
from Assets import Common

system = os.name

def clear():
    os.system('cls')

def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)

#spawn_program_and_die(['python', 'path/to/my/script.py'])

def main():
    os.system('cls')
    Common.setTitle(f"Lotux Puzzles v{Common.THIS_VERSION}")
    Common.transition()
    Common.lotuxhometitle()
    Common.lotuxhometree()
    choice = input("[#] Choice: ")
    if choice == "1" or "01":
        Common.transition()
        spawn_program_and_die(['python', 'python Games/Maze.py'])
    elif choice == "2" or "02":
        Common.transition()
        spawn_program_and_die(['python', 'python Games/TicTacToe.py'])
    
main()
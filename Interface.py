import os, sys, time, subprocess
from Assets import Common

system = os.name

def clear():
    os.system('cls')

def spawn_program_and_die(program, exit_code=0):
    subprocess.Popen(program)
    sys.exit(exit_code)


def main():
    os.system('cls')
    Common.setTitle(f"Lotux Puzzles v{Common.THIS_VERSION}")
    Common.transition()
    Common.lotuxhometitle()
    Common.LineSep()
    Common.lotuxhometree()
    choice = input("[#] Choice: ")
    if choice == "1" or "01":
        Common.transition()
        spawn_program_and_die(['python', 'Games/Maze.py'])
    elif choice == "2" or "02":
        Common.transition()
        spawn_program_and_die(['python', 'Games/TicTacToe.py'])

    
main()

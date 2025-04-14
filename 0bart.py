import shutil
import os
import time
import platform
from datetime import datetime

RESET = "\033[0m"
PRI = "\033[92m"
SEC = "\033[33m"
GRAY = "\033[90m"
WHI = "\033[38;5;255m"
RED = "\033[38;5;168m"

ins = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
outs = [
    [
        "      0011        ",
        "     101100       ",
        "    010  000      ",
        "   100    010     ",
        "  001010001100    ",
        " 100        011   ",
        "100          001  "
    ],
    [
        "11111010    ",
        "10    0111  ",
        "10    0001  ",
        "11111011    ",
        "10    0110  ",
        "10    0011  ",
        "11111010    "
    ],
    [
        "00111110   ",
        "11     10  ",
        "10         ",
        "10         ",
        "10         ",
        "11     00  ",
        "00111111   "
    ],
    [
        "11111001     ",
        "10      11   ",
        "10       10  ",
        "10       10  ",
        "10       01  ",
        "10      11   ",
        "11111010     "
    ],
    [
        "11111111  ",
        "10        ",
        "10        ",
        "11111110  ",
        "10        ",
        "10        ",
        "11111111  "
    ],
    [
        "11111111  ",
        "10        ",
        "10        ",
        "11111110  ",
        "10        ",
        "10        ",
        "10        "
    ],
    [
        "00111110    ",
        "11     10   ",
        "10          ",
        "10   11111  ",
        "10     00   ",
        "11     10   ",
        "00111110    "
    ],
    [
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "11111111  ",
        "10    01  ",
        "10    01  ",
        "10    01  "
    ],
    [
        "1111111  ",
        "   01    ",
        "   01    ",
        "   01    ",
        "   01    ",
        "   01    ",
        "1111111  "
    ],
    [
        "     11111  ",
        "       10   ",
        "       10   ",
        "       10   ",
        "10     10   ",
        "10     01   ",
        "00111110    "
    ],
    [
        "10   01  ",
        "10  10   ",
        "10 11    ",
        "1110     ",
        "10 10    ",
        "10  01   ",
        "10   10  "
    ],
    [
        "10         ",
        "10         ",
        "10         ",
        "10         ",
        "10         ",
        "10         ",
        "111111111  "
    ],
    [
        "10     01  ",
        "110   011  ",
        "10 1 1 01  ",
        "10  1  01  ",
        "10     01  ",
        "10     01  ",
        "10     01  "
    ],
    [
        "10     01  ",
        "110    01  ",
        "10 0   01  ",
        "10  1  01  ",
        "10   0 01  ",
        "10    101  ",
        "10     01  "
    ],
    [
        "00111100  ",
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "00111100  "
    ],
    [
        "1111110   ",
        "10    01  ",
        "10    01  ",
        "1111110   ",
        "10        ",
        "10        ",
        "10        "
    ],
    [
        "00111100    ",
        "10    01    ",
        "10    01    ",
        "10    01    ",
        "10  0 01    ",
        "10   011    ",
        "00111110 0  "
    ],
    [
        "1111110   ",
        "10    01  ",
        "10    01  ",
        "1111110   ",
        "10  10    ",
        "10   01   ",
        "10    10  "
    ],
    [
        "0111111   ",
        "10        ",
        "10        ",
        "0011110   ",
        "      01  ",
        "      01  ",
        "1111110   "
    ],
    [
        "1111111  ",
        "   01    ",
        "   01    ",
        "   01    ",
        "   01    ",
        "   01    ",
        "   01    "
    ],
    [
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "10    01  ",
        "00111100  "
    ],
    [
        "10     01  ",
        "10     01  ",
        "10     01  ",
        " 10   10   ",
        " 10   10   ",
        "  01 01    ",
        "   111     "
    ],
    [
        "10       01  ",
        "10       01  ",
        "10       01  ",
        "10   1   01  ",
        "10  1 1  01  ",
        "10 0   0 01  ",
        "010     10   "
    ],
    [
        "10     01  ",
        " 10   10   ",
        "  01 01    ",
        "   11      ",
        "  01 01    ",
        " 10   10   ",
        "10     01  "
    ],
    [
        "10     01  ",
        " 10   10   ",
        "  01 01    ",
        "   11      ",
        "   01      ",
        "   01      ",
        "   01      "
    ],
    [
        "11111111  ",
        "      10  ",
        "     10   ",
        "    10    ",
        "   10     ",
        "  10      ",
        "11111111  "
    ]
]

term_width = shutil.get_terminal_size((80, 20)).columns
size = 7

def print_chr(chr):
    for line in output:
        for ch in line:
            if ch == '0':
                print(f"{SEC}{ch}{RESET}", end='')
            else:
                print(f"{PRI}{ch}{RESET}", end='')
        print()
    print()

def easter_egg():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print(f"{WHI}{"  * MA INDUSTRIES TERMINAL HIJACK SYSTEM (NOWAR3289)"}{RESET}")
    time.sleep(1)
    print(f"{WHI}{"  // In Progress"}{RESET}")
    time.sleep(3)
    print("\n"*3)
    print (f"{GRAY}{"        The user is a part of the following security groups:"}")
    print ("        _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    time.sleep(0.25)
    print("            Domain users:")
    print("            BUILTIN\\Users")
    print("            NT AUTHORITY\\INTERACTIVE")
    time.sleep(2)
    print("\n"*2)
    print("  OK to Reboot?  [Y/N]_")
    time.sleep(3)
    print("\n"*2)
    print(f"{"  C:\\"}{RESET}")
    time.sleep(0.25)
    print(f"{WHI}{"""
        #      # ####### #        #####   ####### #     # #######    #     # #######      #     #    #    #     # #######  #####  #     #
        #  #   # #       #       #      # #     # ##   ## #          ##   ## #      #     ##   ##   # #   ##    #    #    #     # #     #
        #  #   # #       #       #        #     # # # # # #          # # # # #      #     # # # #  #   #  # #   #    #    #       #     #
        #  #   # #####   #       #        #     # #  #  # #####      #  #  # #######      #  #  # #     # #  #  #    #     #####  #######
        #  #   # #       #       #        #     # #     # #          #     # #    #       #     # ####### #   # #    #          # #     #
        #  #   # #       #       #      # #     # #     # #          #     # #     #  ### #     # #     # #    ##    #          # #     #
         ##  ##  ####### #######  #####   ####### #     # #######    #     # #      # ### #     # #     # #     # ####### ######  #     #
"""}{RESET}")
    time.sleep(2.5)
    os_info = platform.uname()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = f"{RED}{f"""
        **System Error: Critical Failure**
        Error Code: 0xD6F4-9A37
        OS: {os_info.system} {os_info.release} {os_info.version} (Build {os_info.machine})
        Timestamp: {timestamp}
        Severity Level: High

        Fatal System Shutdown Initiated...
        Memory Allocation Failure - Insufficient Resources

        Error Details:
        - Module: System.Core.dll
        - Exception Type: ACCESS_VIOLATION
        - Location: 0x77C6F23A
        - Thread ID: Unknown
        - Process ID: Unknown

        Please restart the system. If the problem persists, contact your system administrator for further assistance.
    """}{RESET}"
    print(error_message)


while True:
    user_input = input().upper()
    print()
    if user_input == 'E':
        break
    elif user_input == 'NOWAR3289':
        easter_egg()
        break
    else:
        output = ['' for _ in range(size)]

        for chr in user_input:
            if chr in ins:
                index = ins.index(chr)
                new_letter = [outs[index][i] for i in range(size)]
            else:
                new_letter = [' ' * 5 for _ in range(size)]
        
            if len(output[0] + new_letter[0]) > term_width:
                print_chr(output)
                output = ['' for _ in range(size)]
            
            for i in range(size):
                output[i] += new_letter[i]
        
        if any (line.strip() for line in output):
            print_chr(output)
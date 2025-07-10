#!/usr/bin/env python3
import os

def main():
    while True:
        print("""
 ██████╗ ███████╗██╗███╗   ██╗████████╗███████╗██████╗ 
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║   ██║███████╗██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║   ██║╚════██║██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝███████║██║██║ ╚████║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

             🕵️  Open Source Intelligence toolkit

[1] Username hunter
[2] Email reputation checker
[3] Image EXIF & geolocation
[4] Domain & IP info
[5] File metadata parser
[6] VirusTotal URL scan
[7] Social media lookup
[0] Exit
""")
        choice = input("> ").strip()
        if choice == "1":
            os.system("python3 modules/username_hunter.py")
        elif choice == "2":
            os.system("python3 modules/email_checker.py")
        elif choice == "3":
            os.system("python3 modules/image_exif.py")
        elif choice == "4":
            os.system("python3 modules/domain_ip_info.py")
        elif choice == "5":
            os.system("python3 modules/file_metadata.py")
        elif choice == "6":
            os.system("python3 modules/virustotal_scan.py")
        elif choice == "7":
            os.system("python3 modules/social_lookup.py")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

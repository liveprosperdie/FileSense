import watcher
import argparse
import organizer


def main():
    parser=argparse.ArgumentParser(description="File Organiser running: 1- manual 2- watch")
    parser.add_argument("--mode", default="", help="To decide the mode of operations 1-manual (for running once manually) 2-watch (for running in back for a dir until stopped)")
    args=parser.parse_args()
    folder_path=input("Enter the folder to organise: ")
    if args.mode == "manual":
        organizer.organise(folder_path)
    elif args.mode == "watch":
        organizer.organise(folder_path)
        watcher.observe(folder_path)
    else:
        print("Wrong args passed please check help")

if __name__=="__main__":
    main()
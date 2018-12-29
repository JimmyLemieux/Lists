import argparse


def show_file():
    print 'Files'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-show-lists",help="SHOW YOUR MADE LISTS",type=str)
    args = parser.parse_args()
if __name__  == '__main__':
    main()

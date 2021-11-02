from recognizer import recognize
from trainer import train
from video_taker import take

def main():
    while True:
        if input("take video? (y/n)") == 'y':
            take(input("name: "))
        else:
            break
    if input("new train? (y/n)") == 'y':
        pickle_file = train()
    else:
        pickle_file = input("pickle file: ")
    recognize(pickle_file)

if __name__ == '__main__':
    main()
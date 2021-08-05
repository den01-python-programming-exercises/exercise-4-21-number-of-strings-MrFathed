def main():
    #write your code below this line
    words = []

    while True:
        word = input("")

        if not word:
            break

        words.append(word)

    print(len(words))

if __name__ == '__main__':
    main()

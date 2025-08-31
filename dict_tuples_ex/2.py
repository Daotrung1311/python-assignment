
d = { 
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_all():
    for k, v in d.items():
        avg = 0
        for i in range(len(v)):
            avg = avg + (v[i]/len(v))
        print(f"{k} ==> {v} ==> {round(avg, 2)}")

def add():
    stock_ticker = input()
    price = input()


def main():
    user = input("Enter operation (print, add or amend):")
    if user.lower() == "print":
        print_all()
    elif user.lower() == "add":
        add()

    else:
        print("Unsupported operation:",user)


if __name__ == "__main__":
    main()
from colorama import init, Fore

init(autoreset=True)

def print_colorized(message, color):
    print(color + message)

def main():
    message = "Hello, World!"
    print_colorized(message, Fore.GREEN)

if __name__ == "__main__":
    main()

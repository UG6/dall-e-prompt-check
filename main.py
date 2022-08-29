from os import system, name, path
from time import sleep


def clear_console() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


try:
    import openai
except:
    print(f"{Colors.RED}Error:{Colors.RESET} OpenAI Module isn't installed. Downloading & Installing required "
          f"packages. Please wait..")
    sleep(2)
    system("pip install openai")
    clear_console()
    print("Info: Required modules are now installed.")
    import openai


key = open(path.join(path.dirname(__file__), "api.txt")).read()
if key == "replace_with_your_api_key" or key == "":
    with open(path.join(path.dirname(__file__), "api.txt"), "w") as f:
        f.write(input(f"{Colors.RED}Error:{Colors.RESET} You forgot to enter your API key into 'api.txt' file.\nVist: "
                      f"https://beta.openai.com/account/api-keys to get your API Key.\n >> Please input your API key: "))
    print("Info: API Key updated in 'api.txt' file for future use.\n")
    key = open(path.join(path.dirname(__file__), "api.txt")).read()

openai.api_key = key


def flagged_or_not(my_prompt: str) -> None:
    r = openai.Moderation.create(
        input=my_prompt,
    )

    categories = r["results"][0]["categories"]
    if r["results"][0]["flagged"] is True:
        print(f" {Colors.RED}>> Flagged:{Colors.RESET} ", end="")
        [print(f"{x}, ", end="") for x in categories if categories[x] is True]
        print("\n")
    else:
        print(f" {Colors.GREEN}>> Not Flagged.{Colors.RESET}\n")


if __name__ == '__main__':
    while True:
        prompt = input("Enter your prompt: ")
        flagged_or_not(prompt)
        again = input("Want to check more prompts? [y/n]: ")
        if again.lower() == "n" or again.lower() == "no":
            break
        else:
            clear_console()

import openai

openai.api_key = open("api.txt").read()

prompt = input("Enter your prompt: ")

r = openai.Moderation.create(
    input=prompt,
)

categories = r["results"][0]["categories"]
if r["results"][0]["flagged"] is True:
    print(" >> Flagged: ", end="")
    [print(f"{x}, ", end="") for x in categories if categories[x] is True]
else:
    print(" >> Not Flagged.")

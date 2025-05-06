from ai import call_gpt

def main():
    your_name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")

    def haiku_generator(your_name, topic):
        prompt = (
            f"Write a traditional haiku poem (5-7-5 syllables) about '{topic}', "
            f"dedicated to someone named {your_name}. "
            "It should be quiet, reflective, and use simple natural imagery."
        )
        response = call_gpt(prompt)
        return response

    result = haiku_generator(your_name, topic)
    print(result)

    

if __name__ == "__main__":
    main()
import os, openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_completion():
    while True:
        prompt=input("Ask OpenAI anything: ")
        completions = openai.Completion.create(prompt=prompt,
                                            engine="text-davinci-002",
                                            max_tokens=100)
        completion = completions.choices[0].text
        completion_list = []
        for word in completion.split():
            clean_word = ''
            i=0
            while i<len(word):
                if word[i].isalnum():
                    clean_word+=word[i]
                i+=1
            if clean_word:
                completion_list.append(clean_word.upper())
        res = ' '.join(completion_list)
        print(completion)
        print('-----------------------')
        print(res)


text_completion()



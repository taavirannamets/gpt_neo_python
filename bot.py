from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

prompt = 'Bitcoin is going to zero'
res = generator(prompt, max_length=50, do_sample=True, temperature=0.9)

print(res[0]['generated_text'])

with open('gpt_text.txt', 'w') as f:
    f.writelines(res[0]['generated_text'])
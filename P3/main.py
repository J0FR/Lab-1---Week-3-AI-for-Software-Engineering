import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

print("Few-Shot Prompting:")
prompt = 'A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is: We were traveling in Africa and we saw these very cute whatpus. To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:'
print(f"prompt: {prompt}")
response = model.generate_content(prompt)
print(f"response: {response.text}")
print(" - - - - - - - - - - - - - - - ")
print("Chain-of-Thought Prompting:")
prompt = 'The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1. A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False. The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24. A: Adding all the odd numbers (17, 19) gives 36. The answer is True. The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24. A: Adding all the odd numbers (11, 13) gives 24. The answer is True. The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2. A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False. The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. A: Complete what should A: have said.'
print(f"prompt: {prompt}")
response = model.generate_content(prompt)
print(f"response: {response.text}")
print(" - - - - - - - - - - - - - - - ")
print("Prompt Chaining:")

document = """
A short history of AI

In the first of six weekly briefs, we ask how AI overcame decades of underdelivering

Over the summer of 1956 a small but illustrious group gathered at Dartmouth College in New Hampshire; it included Claude Shannon, the begetter of information theory, and Herb Simon, the only person ever to win both the Nobel Memorial Prize in Economic Sciences awarded by the Royal Swedish Academy of Sciences and the Turing Award awarded by the Association for Computing Machinery. They had been called together by a young researcher, John McCarthy, who wanted to discuss “how to make machines use language, form abstractions and concepts” and “solve kinds of problems now reserved for humans”. It was the first academic gathering devoted to what McCarthy dubbed “artificial intelligence”. And it set a template for the field’s next 60-odd years in coming up with no advances on a par with its ambitions.

The Dartmouth meeting did not mark the beginning of scientific inquiry into machines which could think like people. Alan Turing, for whom the Turing prize is named, wondered about it; so did John von Neumann, an inspiration to McCarthy. By 1956 there were already a number of approaches to the issue; historians think one of the reasons McCarthy coined the term artificial intelligence, later ai, for his project was that it was broad enough to encompass them all, keeping open the question of which might be best. Some researchers favoured systems based on combining facts about the world with axioms like those of geometry and symbolic logic so as to infer appropriate responses; others preferred building systems in which the probability of one thing depended on the constantly updated probabilities of many others.


The following decades saw much intellectual ferment and argument on the topic, but by the 1980s there was wide agreement on the way forward: “expert systems” which used symbolic logic to capture and apply the best of human know-how. The Japanese government, in particular, threw its weight behind the idea of such systems and the hardware they might need. But for the most part such systems proved too inflexible to cope with the messiness of the real world. By the late 1980s ai had fallen into disrepute, a byword for overpromising and underdelivering. Those researchers still in the field started to shun the term.


It was from one of those pockets of perseverance that today’s boom was born. As the rudiments of the way in which brain cells—a type of neuron—work were pieced together in the 1940s, computer scientists began to wonder if machines could be wired up the same way. In a biological brain there are connections between neurons which allow activity in one to trigger or suppress activity in another; what one neuron does depends on what the other neurons connected to it are doing. A first attempt to model this in the lab (by Marvin Minsky, a Dartford attendee) used hardware to model networks of neurons. Since then, layers of interconnected neurons have been simulated in software.


These artificial neural networks are not programmed using explicit rules; instead, they “learn” by being exposed to lots of examples. During this training the strength of the connections between the neurons (known as “weights”) are repeatedly adjusted so that, eventually, a given input produces an appropriate output. Minsky himself abandoned the idea, but others took it forward. By the early 1990s neural networks had been trained to do things like help sort the post by recognising handwritten numbers. Researchers thought adding more layers of neurons might allow more sophisticated achievements. But it also made the systems run much more slowly.

A new sort of computer hardware provided a way around the problem. Its potential was dramatically demonstrated in 2009, when researchers at Stanford University increased the speed at which a neural net could run 70-fold, using a gaming pc in their dorm room. This was possible because, as well as the “central processing unit” (cpu) found in all pcs, this one also had a “graphics processing unit” (gpu) to create game worlds on screen. And the gpu was designed in a way suited to running the neural-network code.

Coupling that hardware speed-up with more efficient training algorithms meant that networks with millions of connections could be trained in a reasonable time; neural networks could handle bigger inputs and, crucially, be given more layers. These “deeper” networks turned out to be far more capable.

The power of this new approach, which had come to be known as “deep learning”, became apparent in the ImageNet Challenge of 2012. Image-recognition systems competing in the challenge were provided with a database of more than a million labelled image files. For any given word, such as “dog” or “cat”, the database contained several hundred photos. Image-recognition systems would be trained, using these examples, to “map” input, in the form of images, onto output in the form of one-word descriptions. The systems were then challenged to produce such descriptions when fed previously unseen test images. In 2012 a team led by Geoff Hinton, then at the University of Toronto, used deep learning to achieve an accuracy of 85%. It was instantly recognised as a breakthrough.

By 2015 almost everyone in the image-recognition field was using deep learning, and the winning accuracy at the ImageNet Challenge had reached 96%—better than the average human score. Deep learning was also being applied to a host of other “problems…reserved for humans” which could be reduced to the mapping of one type of thing onto another: speech recognition (mapping sound to text), face-recognition (mapping faces to names) and translation.

In all these applications the huge amounts of data that could be accessed through the internet were vital to success; what was more, the number of people using the internet spoke to the possibility of large markets. And the bigger (ie, deeper) the networks were made, and the more training data they were given, the more their performance improved.

Deep learning was soon being deployed in all kinds of new products and services. Voice-driven devices such as Amazon’s Alexa appeared. Online transcription services became useful. Web browsers offered automatic translations. Saying such things were enabled by ai started to sound cool, rather than embarrassing, though it was also a bit redundant; nearly every technology referred to as ai then and now actually relies on deep learning under the bonnet.

Chatgpt and its rivals really do seem to “use language and form abstractions”
In 2017 a qualitative change was added to the quantitative benefits being provided by more computing power and more data: a new way of arranging connections between neurons called the transformer. Transformers enable neural networks to keep track of patterns in their input, even if the elements of the pattern are far apart, in a way that allows them to bestow “attention” on particular features in the data.

Transformers gave networks a better grasp of context, which suited them to a technique called “self-supervised learning”. In essence, some words are randomly blanked out during training, and the model teaches itself to fill in the most likely candidate. Because the training data do not have to be labelled in advance, such models can be trained using billions of words of raw text taken from the internet.

Mind your language model
Transformer-based large language models (llms) began attracting wider attention in 2019, when a model called gpt-2 was released by Openai, a startup (gpt stands for generative pre-trained transformer). Such llms turned out to be capable of “emergent” behaviour for which they had not been explicitly trained. Soaking up huge amounts of language did not just make them surprisingly adept at linguistic tasks like summarisation or translation, but also at things—like simple arithmetic and the writing of software—which were implicit in the training data. Less happily it also meant they reproduced biases in the data fed to them, which meant many of the prevailing prejudices of human society emerged in their output.


In November 2022 a larger Openai model, gpt-3.5, was presented to the public in the form of a chatbot. Anyone with a web browser could enter a prompt and get a response. No consumer product has ever taken off quicker. Within weeks Chatgpt was generating everything from college essays to computer code. ai had made another great leap forward.

Where the first cohort of ai-powered products was based on recognition, this second one is based on generation. Deep-learning models such as Stable Diffusion and dall-e, which also made their debuts around that time, used a technique called diffusion to turn text prompts into images. Other models can produce surprisingly realistic video, speech or music.

The leap is not just technological. Making things makes a difference. Chatgpt and rivals such as Gemini (from Google) and Claude (from Anthropic, founded by researchers previously at Openai) produce outputs from calculations just as other deep-learning systems do. But the fact that they respond to requests with novelties makes them feel very unlike software which recognises faces, takes dictation or translates menus. They really do seem to “use language” and “form abstractions”, just as McCarthy had hoped.

This series of briefs will look at how these models work, how much further their powers can grow, what new uses they will be put to, as well as what they will not, or should not, be used for. q
"""

first_prompt = f"""
You are a helpful assistant. Your task is to help answer a question given in a document. The first step is to extract quotes relevant to the question from the document, delimited by ####. Please output the list of quotes using <quotes></quotes>. Respond with "No relevant quotes found!" if no relevant quotes were found.
####
{document}
####
"""

print(f"Prompt: {first_prompt}")
response = model.generate_content(first_prompt)
quotes = response.text
print(f"Response: {quotes}")

# Second Prompt
second_prompt = f"""
Given a set of relevant quotes (delimited by <quotes></quotes>) extracted from a document and the original document (delimited by ####), please compose an answer to the question. Ensure that the answer is accurate, has a friendly tone, and sounds helpful.
####
{document}
####
<quotes>
{quotes}
</quotes>
"""

print(f"Prompt: {second_prompt}")
final_response = model.generate_content(second_prompt)
print(f"Response: {final_response.text}")
print(" - - - - - - - - - - - - - - - ")
print("Self-Consistency:")
prompt = 'When I was 6 my sister was half my age. Now I’m 70 how old is my sister?'
print(f"prompt: {prompt}")
response = model.generate_content(prompt)
print(f"response: {response.text}")
print(" - - - - - - - - - - - - - - - ")
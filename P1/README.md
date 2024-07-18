# P1. (10 points) Find the definition of these prompt types:

### Zero-shot Prompting

Zero-shot prompting involves providing the model with a task-specific instruction without any examples or demonstrations. This method relies solely on the model's pre-existing knowledge and understanding to generate responses.

### Few-shot Prompting

Few-shot prompting enhances in-context learning by including a few examples within the prompt. These examples help guide the model, improving its ability to generate accurate and relevant responses for subsequent tasks.

### Chain-of-Thought (CoT) Prompting

Chain-of-Thought prompting improves complex reasoning by incorporating intermediate reasoning steps into the prompt. This method breaks down complex tasks into smaller, logical steps, which can be particularly effective when combined with few-shot prompting for tasks requiring detailed reasoning.

### Self-Consistency

Self-consistency is an advanced technique that improves the performance of chain-of-thought prompting. It involves generating multiple reasoning paths and selecting the most consistent one. This approach enhances the model's reliability, especially in tasks involving arithmetic and commonsense reasoning&#8203;:citation[oaicite:7]{index=7}&#8203;.

### Generated Knowledge Prompting

Generated knowledge prompting involves generating relevant knowledge as part of the prompt before making predictions. This technique is particularly useful for tasks that require background information, helping the model to produce more accurate and informed responses&#8203;:citation[oaicite:6]{index=6}&#8203;.

### Prompt Chaining

Prompt chaining breaks down complex tasks into subtasks, where each subtask's response serves as input for the next prompt. This method enhances the model's performance, transparency, and controllability, making it easier to debug and improve responses incrementally&#8203;:citation[oaicite:5]{index=5}&#8203;.

### Tree of Thoughts (ToT)

Tree of Thoughts prompting generalizes chain-of-thought prompting by exploring multiple potential reasoning paths through a tree structure. This method enables the model to evaluate different intermediate steps systematically, using search algorithms like breadth-first and depth-first search for more strategic problem-solving&#8203;:citation[oaicite:4]{index=4}&#8203;.

### Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation combines a language model with external knowledge sources to improve the accuracy and reliability of generated responses. This approach is particularly useful for knowledge-intensive tasks, ensuring factual consistency and reducing errors&#8203;:citation[oaicite:3]{index=3}&#8203;.

### Directional Stimulus Prompting

Directional Stimulus Prompting guides the model's responses by using directional stimuli in the prompt. This technique influences the model's focus and direction, improving its ability to generate targeted and relevant outputs&#8203;:citation[oaicite:2]{index=2}&#8203;.

### ReAct Prompting

ReAct Prompting integrates reasoning and acting by prompting the model to generate reasoning traces and actions. This method combines dynamic reasoning with interaction with external environments, such as search engines, to incorporate additional information and improve task performance&#8203;:citation[oaicite:1]{index=1}&#8203;.

### Multimodal CoT Prompting

Multimodal Chain-of-Thought prompting extends chain-of-thought reasoning to multiple modalities, such as text and images. This approach allows the model to integrate and reason across different types of data, enhancing its capability to handle complex tasks involving various forms of information&#8203;:citation[oaicite:0]{index=0}&#8203;.

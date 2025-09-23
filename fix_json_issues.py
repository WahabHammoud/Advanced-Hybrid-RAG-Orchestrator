#!/usr/bin/env python3
"""
Script to fix JSON output issues in functions_for_pipeline.py
"""

def fix_groq_model_and_prompts():
    with open('functions_for_pipeline.py', 'r') as file:
        content = file.read()
    
    # Replace llama3-70b-8192 with llama3-8b-8192 for better JSON compliance
    content = content.replace('llama3-70b-8192', 'llama3-8b-8192')
    
    # Reduce max_tokens for more focused responses
    content = content.replace('max_tokens=4000', 'max_tokens=2000')
    
    # Fix the planner prompt to be more explicit about JSON
    old_planner_prompt = '''planner_prompt = """ For the given query {question}, come up with a simple step by step plan of how to figure out the answer. 

    This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. 
    The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.
    """'''
    
    new_planner_prompt = '''planner_prompt = """ For the given query {question}, create a simple step-by-step plan to find the answer. 

    IMPORTANT: You must respond with ONLY a JSON object containing a "steps" array. No explanations, no code, no additional text.

    Example format:
    {{"steps": ["Step 1: Search for relevant information", "Step 2: Analyze the findings", "Step 3: Provide final answer"]}}

    Query: {question}
    
    Respond with JSON only:"""'''
    
    content = content.replace(old_planner_prompt, new_planner_prompt)
    
    # Fix task handler prompt to be more explicit about JSON
    old_task_prompt = '''tasks_handler_prompt_template = """You are a task handler that receives a task {curr_task} and have to decide with tool to use to execute the task.
    You have the following tools at your disposal:
    Tool A: a tool that retrieves relevant information from a vector store of book chunks based on a given query.
    - use Tool A when you think the current task should search for information in the book chunks.
    Tool B: a tool that retrieves relevant information from a vector store of chapter summaries based on a given query.
    - use Tool B when you think the current task should search for information in the chapter summaries.
    Tool C: a tool that retrieves relevant information from a vector store of quotes from the book based on a given query.
    - use Tool C when you think the current task should search for information in the book quotes.
    Tool D: a tool that answers a question from a given context.
    - use Tool D ONLY when you the current task can be answered by the aggregated context {aggregated_context}

    you also receive the last tool used {last_tool}
    if {last_tool} was retrieve_chunks, use other tools than Tool A.

    You also have the past steps {past_steps} that you can use to make decisions and understand the context of the task.
    You also have the initial user's question {question} that you can use to make decisions and understand the context of the task.

    Output the tool that should be used to execute the task. choose from: retrieve_chunks, retrieve_summaries, retrieve_quotes, answer_from_context.
    """'''
    
    new_task_prompt = '''tasks_handler_prompt_template = """Task: {curr_task}

    Choose one tool:
    - retrieve_chunks: Search book chunks
    - retrieve_summaries: Search chapter summaries  
    - retrieve_quotes: Search book quotes
    - answer_from_context: Answer from context (only if sufficient context available)

    Available context: {aggregated_context}
    Last tool: {last_tool}
    Past steps: {past_steps}
    Question: {question}

    IMPORTANT: Respond with ONLY this JSON format:
    {{"tool": "retrieve_chunks", "explanation": "Brief reason"}}

    JSON Response:"""'''
    
    content = content.replace(old_task_prompt, new_task_prompt)
    
    with open('functions_for_pipeline.py', 'w') as file:
        file.write(content)
    
    print("✅ Fixed Groq model settings and prompts for better JSON output!")

if __name__ == "__main__":
    fix_groq_model_and_prompts()
#!/usr/bin/env python3
"""
Script to automatically replace OpenAI with Groq in functions_for_pipeline.py
"""

def fix_groq_configuration():
    # Read the file
    with open('functions_for_pipeline.py', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Make the replacements
    replacements = [
        # Import changes
        ('from langchain_openai import ChatOpenAI', '# from langchain_openai import ChatOpenAI'),
        ('# from langchain_groq import ChatGroq', 'from langchain_groq import ChatGroq'),
        ('from langchain_openai import OpenAIEmbeddings', 'from langchain_community.embeddings import HuggingFaceEmbeddings'),
        
        # Environment variable changes
        ('os.environ["OPENAI_API_KEY"] = os.getenv(\'OPENAI_API_KEY\')', '# os.environ["OPENAI_API_KEY"] = os.getenv(\'OPENAI_API_KEY\')'),
        ('# groq_api_key = os.getenv(\'GROQ_API_KEY\')', 'groq_api_key = os.getenv(\'GROQ_API_KEY\')'),
        
        # Replace embeddings
        ('embeddings = OpenAIEmbeddings()', 'embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")'),
        
        # Replace all ChatOpenAI instances
        ('ChatOpenAI(temperature=0, model_name="gpt-4o", max_tokens=2000)', 'ChatGroq(temperature=0, model_name="llama3-70b-8192", groq_api_key=groq_api_key, max_tokens=4000)'),
    ]
    
    # Apply replacements
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Write back to file
    with open('functions_for_pipeline.py', 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("✅ Successfully converted functions_for_pipeline.py to use Groq!")
    print("✅ Now you can run: docker-compose up --build")

if __name__ == "__main__":
    fix_groq_configuration()
from pymongo import MongoClient

def query_knowledge_base(user_query):

    uri = "mongodb://gopal612:1258@localhost:27777/?directConnection=true" 
    client = MongoClient(uri)
    
    # This is a mock search - it just proves the connection works
    print(f"--- Debug: Searching MongoDB for '{user_query}' ---")
    
    # In a real setup, you'd use your Vector Search index here
    return "Manual says: Turn the red knob to 'Off' before servicing."
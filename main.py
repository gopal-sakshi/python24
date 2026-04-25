from graph23 import app         ## see "graph23.py" file babai

if __name__ == "__main__":
    print("--- Technician Assistant Startup ---")
    user_input = input("Enter technician query: ")
    
    # Run the graph
    result = app.invoke({"query": user_input})
    
    print("\nFINAL RESPONSE:")
    print(result["response"])
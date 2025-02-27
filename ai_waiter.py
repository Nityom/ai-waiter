import json
import ollama

# Load menu data
with open("menu.json", "r", encoding="utf-8") as file:
    menu_data = json.load(file)

def query_menu(user_input):
    user_input = user_input.lower()
    
    # Extract dish names
    dish_names = [item["name"].lower() for item in menu_data]

    # Check for best-selling items
    if "best-selling" in user_input or "most popular" in user_input:
        best_sellers = sorted(menu_data, key=lambda x: x.get("orders", 0), reverse=True)[:3]
        return f"Our best-selling dishes are: {', '.join([item['name'] for item in best_sellers])}."

    # Check for dishes below a certain price
    if "below" in user_input and "dollar" in user_input:
        price_limit = int(''.join(filter(str.isdigit, user_input)))  # Extract number
        cheap_dishes = [item["name"] for item in menu_data if int(item["price"].replace("$", "")) < price_limit]
        if cheap_dishes:
            return f"Here are some dishes under ${price_limit}: {', '.join(cheap_dishes)}."
        return f"Sorry, we don't have dishes below ${price_limit}."

    # Check if user asks about ingredients
    for item in menu_data:
        if item["name"].lower() in user_input:
            if "ingredient" in user_input or "contain" in user_input:
                return f"{item['name']} contains: {', '.join(item.get('ingredients', []))}."
            return f"Yes, {item['name']} is available."

    # If no menu-related match, use LLaMA 2 but restrict to menu data
    menu_context = "\n".join([f"{item['name']}: ${item['price']}, Ingredients: {', '.join(item.get('ingredients', []))}" for item in menu_data])

    prompt = f"""
    You are an AI Waiter. Answer like a friendly restaurant assistant. 
    Only use this menu for responses:
    
    {menu_context}
    
    User: {user_input}
    AI Waiter:
    """

    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

# Main loop
while True:
    user_input = input("Ask me about the menu: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("AI Waiter:", query_menu(user_input))

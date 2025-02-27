# AI Waiter

AI Waiter is a conversational AI assistant that interacts with users to provide menu-related information. It uses **LLaMA 2 via Ollama** for natural responses while strictly referencing `menu.json` to avoid hallucinations.

## Features 🚀
- 💬 **Conversational AI**: Uses LLaMA 2 to provide human-like interactions.
- 📋 **Menu-Based Responses**: Only references dishes in `menu.json`.
- 🌟 **Best-Selling Dishes**: Lists the most popular items.
- 💰 **Price Filtering**: Finds dishes below a specified price.
- 🥘 **Ingredient Information**: Provides dish ingredients upon request.
- 🛠 **Easy Customization**: Modify `menu.json` to update menu items.

## Installation & Setup 🛠️
### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai/) installed

### Steps to Run
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/ai-waiter.git
   cd ai-waiter
   ```
2. **Install Dependencies**
   ```sh
   pip install ollama
   ```
3. **Ensure LLaMA 2 is Installed**
   ```sh
   ollama pull llama2
   ```
4. **Prepare `menu.json`** (Example format below)
   ```json
   [
       {"name": "Chicken Biryani", "price": "$12", "orders": 120, "ingredients": ["Chicken", "Rice", "Spices"]},
       {"name": "Margherita Pizza", "price": "$10", "orders": 95, "ingredients": ["Dough", "Tomato Sauce", "Mozzarella", "Basil"]}
   ]
   ```
5. **Run the Script**
   ```sh
   python ai_waiter.py
   ```

## Usage 💡
Interact with the AI Waiter via command-line:
```
Ask me about the menu: What are the best-selling items?
AI Waiter: Our best-selling dishes are: Chicken Biryani, Margherita Pizza.

Ask me about the menu: Does Margherita Pizza contain peanuts?
AI Waiter: No, Margherita Pizza contains: Dough, Tomato Sauce, Mozzarella, Basil.

Ask me about the menu: What dishes are under 10 dollars?
AI Waiter: Here are some dishes under $10: Veggie Burger, Caesar Salad.
```

## Customization ✨
- Modify `menu.json` to update dishes, prices, and ingredients.
- Change response styles in `query_menu()`.



---
🚀 **Enjoy your AI Waiter experience!** 🍽️


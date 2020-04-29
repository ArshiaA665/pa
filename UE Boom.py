_product_list = {
    "UE Boom": 79.99,
    "GoPro Hero 8": 549.00,
    "Henry Hoover": 499.49,
    "Icky Thump LP": 35.37,
    "Kraft Dinner": 3.87,
    "Umbrella": 26.95,
    "Vans": 72.16,
    "Water Bottle": 45.00,
    "Weird Baby Burrito Blanket": 15.99
}
def get_command():
    user_input = input('Enter a command: ')
    input_list = user_input.split()
    command = input_list.pop(0)
    return command, input_list
        
def add_to_cart(cart_items, arg_list):
    item = " "join(arg_list)
    price = _product_list[item]
    _cart_items.append(item)
    
def show_command(cart_items):
    print(f"cart items = {_cart_items}")
    
    
def remove_command(cart_items, arg_list):
    item = "  "join(arg_list)
    price = _product_list[item]
    _cart_items.remove(item)
 
 
def main():

    _cart_items = []
    
    cmd, arg_list = get_cmd()
    while cmd != 'quit':
    
        if cmd == 'add':
            add_to_cart(_cart_items, arg_list)
        if cmd == 'show':
            show_cart(_cart_items)
        if cmd == 'remove':
            remove_cart(_cart_items, arg_list)
            
            
            
        cmd, arg_list = get_cmd()
        
    exit()
    
main()
    

import telebot

# Substitua 'TOKEN' pelo token do seu bot fornecido pelo BotFather
bot = telebot.TeleBot('7177741460r3:AAEFjJtyizvnlr29zQOVSgqzdnUjPSXuMYVLo5433buf=53f3')
# esse token nao funciona para minha segurança


# Dicionário de hambúrgueres com seus preços
menu = {
    "Hambúrguer Simples": 10.99,
    "Hambúrguer Duplo": 14.99,
    "Hambúrguer Vegano": 12.99,
    "Cheeseburger": 11.99,
    "Hambúrguer Especial": 16.99
}

# Lista para armazenar os pedidos
pedidos = []



# manipulando start
@bot.message_handler(commands=['start', 'ajuda'])
def info(message):
    bot.reply_to(message, 'Olá! Bem-vindo á Hamburgueria Walter. Como posso ajudar? /cardapio ou /fazerPedido')



# Manipulador de comando para o comando /cardapio
@bot.message_handler(commands=['cardapio'])
def cardapio(message):
    response = "<b>Cardápio de Hambúrgueres:</b>\n\n"
    for item, price in menu.items():
        response += f"<b>{item}</b>: R${price:.2f}\n"
    response += "\nPara fazer um pedido, digite /pedido seguido do hambúrguer desejado."
    bot.send_message(message.chat.id, response, parse_mode='HTML')

# Manipulador de comando para o comando /pedido
@bot.message_handler(commands=['pedido'])
def pedido(message):
    command_args = message.text.split()[1:]
    if not command_args:
        bot.send_message(message.chat.id, "Por favor, especifique o hambúrguer desejado após o comando /pedido.")
    else:
        burger_name = ' '.join(command_args)
        if burger_name in menu:
            total_price = menu[burger_name]
            pedidos.append((message.from_user.first_name, burger_name, total_price))
            bot.send_message(message.chat.id, f"Pedido recebido! Você pediu um {burger_name}. Total: R${total_price:.2f}")
        else:
            bot.send_message(message.chat.id, "Desculpe, o hambúrguer especificado não está no cardápio.")

# Manipulador de comando para o comando /verpedidos
@bot.message_handler(commands=['verpedidos'])
def ver_pedidos(message):
    response = "<b>Pedidos Realizados:</b>\n\n"
    for i, pedido in enumerate(pedidos, start=1):
        response += f"<b>Pedido {i}:</b>\n"
        response += f"<b>Cliente:</b> {pedido[0]}\n"
        response += f"<b>Hambúrguer:</b> {pedido[1]}\n"
        response += f"<b>Total:</b> R${pedido[2]:.2f}\n\n"
    if pedidos:
        bot.send_message(message.chat.id, response, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "Não há pedidos realizados até o momento.")


#varificar qualquer outra mensagem
def verificar(menssagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá! Bem-vindo á Hamburgueria Walter. Como posso ajudar? 
    Escolha uma opção para continuar (Clique no item):
     /cardapio Veja o cardapio
     /pedido Fazer pedidos
     /verpedidos Ver seus pedidos
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


# Inicia o bot
bot.polling()

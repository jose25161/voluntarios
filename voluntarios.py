from tkinter import *
from tkinter import messagebox

from pymongo import MongoClient

def startup_db_client():
	connection_string = 'mongodb+srv://hub_altruista:<password>@hub-altruista.a1hja.mongodb.net/?retryWrites=true&w=majority&appName=hub-altruista'
	client = MongoClient(connection_string)
	db = client['hub-altruista']
	collection = db['usuarios']
	return collection

def get_voluntarios(collection):
	query = { "is_voluntario": True}
	voluntarios = collection.find(query)
	return voluntarios

def get_pedidos(collection):
	query = { "is_voluntario": False}
	pedidos = collection.find(query)
	return pedidos

def save_usuario(collection, cadastro):
	collection.insert_one(cadastro)

def OpenPedidos(client):
	janela_voluntario = Tk()
	janela_voluntario.geometry('350x700')
	janela_voluntario.title("pedidos de ajuda")

	card_size = 4

	pedidos_list = get_pedidos(client)
	for index, x in enumerate(pedidos_list):
		txt_nome = Label(janela_voluntario, text="Nome:", font=('arial', 12))
		txt_nome.grid(row=(0+(index*card_size)), sticky="e")
		value_nome = Label(janela_voluntario, text=x['nome'], font=('arial', 12), bg='lightblue')
		value_nome.grid(row=(0+(index*card_size)),column = 1, sticky="W")

		txt_descricao = Label(janela_voluntario, text="Descricao:", font=('arial', 12))
		txt_descricao.grid(row=(1+(index*card_size)), sticky="NSEW")
		value_descricao = Label(janela_voluntario, text=x['descricao'], font=('arial', 12), bg='lightblue')
		value_descricao.grid(row=(1+(index*card_size)),column = 1, sticky="W")

		txt_contato = Label(janela_voluntario, text="Contato:", font=('arial', 12))
		txt_contato.grid(row=(2+(index*card_size)), sticky="e")
		value_contato = Label(janela_voluntario, text=x['contato'], font=('arial', 12), bg='lightblue')
		value_contato.grid(row=(2+(index*card_size)),column = 1, sticky="W")

		break_line = Label(janela_voluntario, text=" ")
		break_line.grid(row=(3+(index*card_size)), sticky="e")

def OpenCadastro(client):
	janela_cadastro = Tk()
	janela_cadastro.geometry('350x200')
	janela_cadastro.title("cadastro")
	

	txt_nome = Label(janela_cadastro, text="Nome:", font=('arial', 16))
	txt_nome.grid(row=0, sticky="e")
	txt_descricao = Label(janela_cadastro, text="Descricao:", font=('arial', 16))
	txt_descricao.grid(row=1, sticky="e")
	txt_contato = Label(janela_cadastro, text="Contato:", font=('arial', 16))
	txt_contato.grid(row=2, sticky="e")


	input_nome = StringVar()
	DESCRICAO = StringVar()
	CONTATO = StringVar()
	IS_VOLUNTARIO = StringVar(janela_cadastro, "1")

	nome = Entry(janela_cadastro, width=30)
	nome.grid(row=0, column=1)
	descricao = Entry(janela_cadastro, width=30)
	# descricao.place(width=30, height=10)
	descricao.grid(row=1, column=1, columnspan=2)

	contato = Entry(janela_cadastro, textvariable=CONTATO, width=30)
	contato.grid(row=2, column=1)


	checkbox_voluntario = Radiobutton(janela_cadastro, text='Quero ser voluntario',variable=IS_VOLUNTARIO, value=1)
	checkbox_voluntario.grid(row=3, column=0)
	checkbox_pedido = Radiobutton(janela_cadastro, text='Quero fazer um pedido',variable=IS_VOLUNTARIO, value=2)
	checkbox_pedido.grid(row=3, column=1)
	btn_cadastrar = Button(janela_cadastro, text ="Cadastrar")
	btn_cadastrar.grid(row=4, column=1)

	label = Label(janela_cadastro, text = 'cadastro')

	def insert_value(client):
		usuario_value = {'nome': nome.get(), 'descricao': descricao.get(), 'contato': contato.get(), 'is_voluntario': IS_VOLUNTARIO.get() == '1'}
		save_usuario(client, usuario_value)

		messagebox.showinfo(title=None, message='informacao cadastrada')
		janela_cadastro.after(1000 , lambda: janela_cadastro.destroy())

	btn_cadastrar.bind("<Button>", lambda e: insert_value(client))

def OpenVoluntarios(client):
	janela_voluntario = Tk()
	janela_voluntario.geometry('350x700')
	janela_voluntario.title("voluntarios disponiveis")

	card_size = 4

	voluntarios_list = get_voluntarios(client)
	for index, x in enumerate(voluntarios_list):
		txt_nome = Label(janela_voluntario, text="Nome:", font=('arial', 12))
		txt_nome.grid(row=(0+(index*card_size)), sticky="e")
		value_nome = Label(janela_voluntario, text=x['nome'], font=('arial', 12), bg='lightblue')
		value_nome.grid(row=(0+(index*card_size)),column = 1, sticky="W")

		txt_descricao = Label(janela_voluntario, text="Descricao:", font=('arial', 12))
		txt_descricao.grid(row=(1+(index*card_size)), sticky="NSEW")
		value_descricao = Label(janela_voluntario, text=x['descricao'], font=('arial', 12), bg='lightblue')
		value_descricao.grid(row=(1+(index*card_size)),column = 1, sticky="W")

		txt_contato = Label(janela_voluntario, text="Contato:", font=('arial', 12))
		txt_contato.grid(row=(2+(index*card_size)), sticky="e")
		value_contato = Label(janela_voluntario, text=x['contato'], font=('arial', 12), bg='lightblue')
		value_contato.grid(row=(2+(index*card_size)),column = 1, sticky="W")

		break_line = Label(janela_voluntario, text=" ")
		break_line.grid(row=(3+(index*card_size)), sticky="e")



client = startup_db_client()

master = Tk()
master.geometry("250x200")
label = Label(master, text ="HUB Altruista")
master.title("HUB Altruista")
label.pack(side = TOP, pady = 10)

btnVoluntarios = Button(master, 
             text ="voluntarios")

btnPedidos = Button(master, 
             text ="pedidos") 

btnCadastro = Button(master, 
             text ="cadastro")


btnVoluntarios.bind("<Button>", 
         lambda e: OpenVoluntarios(client))
 
btnPedidos.bind("<Button>", 
         lambda e: OpenPedidos(client))

btnCadastro.bind("<Button>", 
         lambda e: OpenCadastro(client))

btnVoluntarios.pack(side= TOP, pady = 10)
btnPedidos.pack(side= TOP, pady = 10)
btnCadastro.pack(side= TOP, pady = 10)

mainloop()
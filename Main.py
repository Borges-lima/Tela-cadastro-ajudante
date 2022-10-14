import tkinter as tk
from tkinter import ttk
from pessoas import Pessoas

#criando a janela
janela = tk.Tk()

#criando campos nome
label_tituajudante = tk.Label(text='AJUDANTE')
label_tituajudante.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_nome = tk.Label(text='Nome')
label_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entr_nome = tk.Entry()
entr_nome.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

#criando campo documento
label_documento = tk.Label(text='RG ou CPF')
label_documento.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
entr_documento = tk.Entry()
entr_documento.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

#criando campo telefone
label_tel = tk.Label(text='Telefone')
label_tel.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)
entr_tel = tk.Entry()
entr_tel.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)

#criando dados bancários
label_dadosBanc = tk.Label(text='DADOS BANCÁRIOS')
label_dadosBanc.grid(row=8, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_banco = tk.Label(text='Cód Banco')
label_banco.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
entr_banco = tk.Entry()
entr_banco.grid(row=10, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
label_agencia = tk.Label(text='Agência')
label_agencia.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
entr_agencia = tk.Entry()
entr_agencia.grid(row=10, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)
label_contCorrente = tk.Label(text='Conta corrente')
label_contCorrente.grid(row=9, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)
entr_contCorrente = tk.Entry()
entr_contCorrente.grid(row=10, column=2, padx=10, pady=10, sticky='nswe', columnspan=1)

#Botão de incluir
botao_incluir = tk.Button(text='Incluir')
botao_incluir.grid(row=11, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)



janela.title('CADASTRO DE AJUDANTE')

janela.mainloop()

















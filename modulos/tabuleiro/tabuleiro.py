def mostrar_tabuleiro(n_de_errou=0):
    if n_de_errou == 0:
        print(''''\033[1;94m
+----+
|     
|      
|   
|   
|    
|''')
    if n_de_errou == 1:
        print(''''\033[1;94m
+----+
|    |   
|      ERROU!
|   
|   
|    
|''')

    if n_de_errou == 2:
        print(''''\033[1;94m
+----+
|    |
|    O   ERROU DE NOVO!
|   
|   
|    
|''')

    if n_de_errou == 3:
        print('''\033[1;94m
+---+
|   |   
|   O  
|  /|\  ERROU MAIS UMA VEZ!
|  
|         
|''')

    if n_de_errou == 4:
        print('''\033[1;31m
+---+
|   |   
|   O  MORREU!
|  /|\  
|  / \ 
|         
|''')


def morto():
    print('''\033[1;31m
+---+
|   |   
|   O  MORREU!
|  /|\  
|  / \ 
|         
|''')

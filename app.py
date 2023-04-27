from flask import Flask, render_template
import busca_sem_info_grid_cruzamentos
import busca_com_pesos_grid_FATEC
app = Flask(__name__)

@app.route("/")
def home():
    dim_x = 6
    dim_y = 6
    origem  = [0,0]
    destino = [5,5]
    mapa, obs = busca_sem_info_grid_cruzamentos.gera_Ambiente(dim_x,dim_y)
    limite = 12

    caminho = busca_sem_info_grid_cruzamentos.sol.prof_limitada(origem,destino,dim_x,dim_y,obs,limite)

   # caminho, custo = busca_com_pesos_grid_FATEC.sol.a_estrela(origem,destino,dim_x,dim_y,obs)
    caminho1 = []

    for no in caminho:
        aux = f'{mapa[no[0]][no[1]]}'
        caminho1.append(aux)

    map = []
    
    for i in mapa:
            for j in mapa:
                x = mapa.index(i)
                y = mapa.index(j)
                map.append(f'{mapa[x][y]}')

    tamanhoLista = len(map)
    testeElementos = []
    y=0;
    for x in range(len(map)):
        if map[x] == caminho1[y]:
            testeElementos.append(map[x])
            y += 1
        else:
            testeElementos.append(0)
    
    return testeElementos
    return render_template('index.html', resultado=testeElementos)

if __name__ == "__main__":
    app.run(debug=True)
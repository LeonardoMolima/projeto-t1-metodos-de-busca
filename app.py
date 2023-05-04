from flask import Flask, render_template, request
import busca_sem_info_grid_cruzamentos
import busca_com_pesos_grid_FATEC
app = Flask(__name__)

def converteCoordenada(valor): 
    valorX = int(valor[0])
    valorY = int(valor[1])
    coord = []
    coord.append(valorX)
    coord.append(valorY)

    return coord


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/grid', methods=["POST"])
def grid():
    valorInicio = request.form.get('optionInit')
    valorFim    = request.form.get('optionEnd')
    metodoForm  = request.form.get('optionAlgorithm') 
    limiteForm  = request.form.get('limite')

    coordInicio = converteCoordenada(valorInicio)
    coordFim = converteCoordenada(valorFim)
    limiteInt   = int(limiteForm)
    metodo      = int(metodoForm)

    dim_x = 6
    dim_y = 6
    origem  = coordInicio
    destino = coordFim
    mapa, obs = busca_sem_info_grid_cruzamentos.gera_Ambiente(dim_x,dim_y)
    limite = limiteInt

    custo = 0
    caminho = []

    if(metodo == 1):
        caminho = busca_sem_info_grid_cruzamentos.sol.amplitude(origem,destino,dim_x,dim_y,obs)
    elif(metodo == 2):
        caminho = busca_sem_info_grid_cruzamentos.sol.profundidade(origem,destino,dim_x,dim_y,obs)
    elif(metodo == 3):
        caminho = busca_sem_info_grid_cruzamentos.sol.prof_limitada(origem,destino,dim_x,dim_y,obs,limite)
    elif(metodo == 4):
        caminho = busca_sem_info_grid_cruzamentos.sol.aprof_iterativo(origem,destino,dim_x,dim_y,obs,limite)
    elif(metodo == 5):
        caminho = busca_sem_info_grid_cruzamentos.sol.bidirecional(origem,destino,dim_x,dim_y,obs)
    elif(metodo == 6):
        caminho, custo = busca_com_pesos_grid_FATEC.sol.custo_uniforme(origem,destino,dim_x,dim_y,obs)
    elif(metodo == 7):
        caminho, custo = busca_com_pesos_grid_FATEC.sol.greedy(origem,destino,dim_x,dim_y,obs)
    elif(metodo == 8):
        caminho, custo = busca_com_pesos_grid_FATEC.sol.a_estrela(origem,destino,dim_x,dim_y,obs)
    elif(metodo == 9):
        caminho, custo = busca_com_pesos_grid_FATEC.sol.aia_estrela(origem,destino,dim_x,dim_y,obs,busca_com_pesos_grid_FATEC.sol.heuristica(origem,destino))

    if caminho == []:
        custo = False
        testeElementos = False
        return render_template('gridResultado.html', resultado=testeElementos, custo=custo)

    caminho1 = []
    
    for no in caminho:
        print("No caminho= ",no)
        aux = f'{mapa[no[0]][no[1]]}'
        caminho1.append(aux)

    map = []
    
    for i in mapa:
            for j in mapa:
                x = mapa.index(i)
                y = mapa.index(j)
                map.append(f'{mapa[x][y]}')

    testeElementos = []

    for x in range(len(map)):
        if map[x] in caminho1:
            testeElementos.append(map[x])
        else:
            testeElementos.append(0)

    print(testeElementos);
    
    return render_template('gridResultado.html', resultado=testeElementos, custo=custo)


if __name__ == "__main__":
    app.run(debug=True)
# Reconhecimento de cores com OpenCV 4.1.1
# *** EM DESENVOLVIMENTO ***

<p> O objetivo deste projeto é realizar alguns estudos/testes na área de visão computacional, especialmente em reconhecimento das cores de objetos. </p>

<p> Nesse estudo vamos utilizar a biblioteca <b> OpenCV (versão 4.1.1) </b> para realizar alguns testes de reconhecimento de cores. </p>

<p> Os exemplos utilizados neste estudo foram baseados no site: </p>

<p>https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html</p>


## Informação sobre os arquivos:

<p> <b>encontrar_valores_hsv.py </b> - Esse programa ajuda a encontrar valores de limite HSV, onde H = Hue (matiz), S = Saturation (saturação) e V = Value (valor), da cor que deseja reconhecer. Esses valores serão utilizados nas variáveis <b>lower_XXX </b> e <b> upper_XXX</b> do programa <b>segmentacao_cores.py </b> </p>

##### Exemplo da seleção dos limites para a cor azul:

![limites_hsv_cor_azul](limites_hsv_cor_azul.jpg)
   
<p> <b>segmentacao_cores.py </b> - Esse programa realiza o reconhecimento das cores. </p>

##### Exemplo de cores reconhecidas:

![cores_reconhecidas](cores_reconhecidas.gif)
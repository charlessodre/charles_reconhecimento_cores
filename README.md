# Reconhecimento de cores com OpenCV 4.1.1

<p> O objetivo deste projeto é realizar alguns estudos/testes na área de visão computacional, especialmente em reconhecimento das cores de objetos. </p>

<p> Nesse estudo vamos utilizar a biblioteca <b> OpenCV (versão 4.1.1) </b> para realizar alguns testes de reconhecimento de cores. </p>

<p> Os exemplos utilizados neste estudo foram baseados nos sites: </p>

<p>https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html</p>
<p>https://blog.socratesk.com/blog/2018/08/16/opencv-hsv-selector</p>


## Informação sobre os arquivos:
<p> <b>reconhecimento_cores.py </b> - Esse é o programa principal que realiza o reconhecimento das cores. </p>
<p> <b>encontrar_valores_hsv.py </b> - Esse programa ajuda a encontrar valores de limite HSV da cor que deseja reconhecer. 
Esses valores serão utilizados nas variáveis <b>lower_XXX </b> e <b> upper_XXX</b> do programa <b>segmentacao_cores.py </b> </p>
<p> <b>OBS: É importante ter em mente que a luz do ambiente influencia diretamente na variação das cores que estamos mapeando/reconhecendo. </b></p>

<p> "HSV é a abreviatura para o sistema de cores formadas pelas componentes Hue, Saturation e Value." (https://pt.wikipedia.org/wiki/HSV). 
Onde:  H = Hue (matiz), S = Saturation (saturação) e V = Value (valor). </p>

##### Abaixo temos uma representação do modelo de cores HSV:
<img src="hsv.png" width="400px" hight="400px">

*imagem retirada do site https://blog.socratesk.com/blog/2018/08/16/opencv-hsv-selector*
 
##### Exemplo da seleção dos limites de algumas cores:


**Vermelho**   
<img src="limites_hsv_cor_vermelha.jpg" hight="400px" width="400px">

**Verde**   
<img src="limites_hsv_cor_verde.jpg" hight="400px" width="400px">

**Azul**   
<img src="limites_hsv_cor_azul.jpg" hight="400px" width="400px">

**Laranja**   
<img src="limites_hsv_cor_laranja.jpg" hight="400px" width="400px">

**Amarelo**   
<img src="limites_hsv_cor_amarela.jpg" hight="400px" width="400px">

**Roxo**   
<img src="limites_hsv_cor_roxo.jpg" hight="400px" width="400px">

**Rosa**   
<img src="limites_hsv_cor_rosa.jpg" hight="400px" width="400px">   

**Marrom**   
<img src="limites_hsv_cor_marrom.jpg" hight="400px" width="400px">  

**Branco**   
<img src="limites_hsv_cor_branca.jpg" hight="400px" width="400px">   

##### Exemplo de cores reconhecidas:

![cores_reconhecidas](cores_reconhecidas.gif)
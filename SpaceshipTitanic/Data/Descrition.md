# Spaceship Titanic

Bem-vindo ao ano de 2912, onde suas habilidades em ciência de dados são necessárias para resolver um mistério cósmico. Recebemos uma transmissão de quatro anos-luz de distância, e as coisas não parecem boas.

O Spaceship Titanic era um navio interestelar de passageiros lançado há um mês. Com quase 13.000 passageiros a bordo, a embarcação partiu em sua viagem inaugural transportando emigrantes do nosso sistema solar para três exoplanetas recém-habitáveis orbitando estrelas próximas.

Ao passar por Alpha Centauri a caminho de seu primeiro destino—o tórrido 55 Cancri E—o desavisado Spaceship Titanic colidiu com uma anomalia espaço-temporal escondida dentro de uma nuvem de poeira. Infelizmente, ele teve um destino semelhante ao seu homônimo de 1000 anos atrás. Embora a nave tenha permanecido intacta, quase metade dos passageiros foi transportada para uma dimensão alternativa!

Para ajudar as equipes de resgate e recuperar os passageiros perdidos, você é desafiado a prever quais passageiros foram transportados pela anomalia usando registros recuperados do sistema de computadores danificados da nave.

Ajude a salvá-los e a mudar a história!

## Dados

**train.csv** - Registros pessoais de cerca de dois terços (~8700) dos passageiros, a serem usados como dados de treinamento.  
- **PassengerId** - Um ID único para cada passageiro. Cada ID tem a forma `gggg_pp`, onde `gggg` indica um grupo com o qual o passageiro está viajando e `pp` é o número dele dentro do grupo. Pessoas em um grupo geralmente são familiares, mas nem sempre.  
- **HomePlanet** - O planeta de onde o passageiro partiu, normalmente seu planeta de residência permanente.  
- **CryoSleep** - Indica se o passageiro optou por ser colocado em animação suspensa durante a viagem. Passageiros em cryosleep ficam confinados em suas cabines.  
- **Cabin** - O número da cabine onde o passageiro está hospedado. Segue o formato `deck/num/side`, onde `side` pode ser `P` (Port - Bombordo) ou `S` (Starboard - Estibordo).  
- **Destination** - O planeta onde o passageiro desembarcará.  
- **Age** - A idade do passageiro.  
- **VIP** - Indica se o passageiro pagou por um serviço VIP especial durante a viagem.  
- **RoomService, FoodCourt, ShoppingMall, Spa, VRDeck** - Valores que o passageiro gastou em cada um dos muitos luxos do Spaceship Titanic.  
- **Name** - O primeiro e último nome do passageiro.  
- **Transported** - Indica se o passageiro foi transportado para outra dimensão. Esta é a coluna alvo, o que você deve prever.  

**test.csv** - Registros pessoais do terço restante (~4300) dos passageiros, a serem usados como dados de teste. Sua tarefa é prever o valor de `Transported` para os passageiros neste conjunto.  

**sample_submission.csv** - Um arquivo de submissão no formato correto.  
- **PassengerId** - ID de cada passageiro no conjunto de teste.  
- **Transported** - O alvo. Para cada passageiro, preveja `True` ou `False`. 
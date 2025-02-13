# Kaggles
Repositório para a resolução de Kaggles

## Inicializando o ambiente
Instale o Anaconda Navigator: https://www.anaconda.com/download/success

Certifique-se de que ele se encontra no PATH, para isto você pode testar o comando abaixo no terminal, caso ele retorne a versão o Anaconda se encontra no Path:

```
conda -V
```

Caso dê erro será necessário colocar as seguintes pastas no PATH:

- ~\Anaconda3\
- ~\Anaconda3\Scripts
- ~\Anaconda3\Library\bin
- ~\Anaconda3\Library\usr\bin

Para configurar o ambiente siga os procedimentos abaixo1:

```
conda env create --file environment.yml

conda activate KaggleGel
```

## Variáveis de ambiente de Kaggle

É importante que você configura as variáveis de ambiente do kaggle para fazer o download dos datasets. Para isto vá até https://www.kaggle.com/settings e crie um novo token da API (kaggle.json). Os dados desse json devem ser inseridos nas variáveis de ambiente para a sua conta da seguinte forma:

| Chave | Valor |
|----------|----------|
| KAGGLE_USERNAME  | username  |
| KAGGLE_KEY  | key  |

## Alterações no ambiente
Sempre que alterar as bibliotecas do projeto atualize o [enviroment.yml](enviroment.yml) fazendo:

```
conda env export --no-builds > environment.yml
```

Também mantenha atualizado seu ambiente fazendo:

```
conda env update --file environment.yml --prune
```
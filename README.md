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

Sempre que adicionar uma biblioteca ao projeto atualize o [enviroment.yml](enviroment.yml) fazendo:

```
conda env export --no-builds > environment.yml
```

Também mantenha atualizado seu ambiente fazendo:

```
conda env update --file environment.yml --prune
```

*Importante:* Ao adicionar bibliotecas com pip coloque sobre a tag pip nas dependencies.
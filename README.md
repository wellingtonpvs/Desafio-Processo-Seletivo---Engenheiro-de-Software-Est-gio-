# Desafio-Processo-Seletivo-Engenheiro-de-Software-Estagio-
Desafio para vaga de estágio

## Projeto Caixa Eletrônico API

Este projeto é uma API simples desenvolvida em Flask para simular um sistema de caixa eletrônico. A API permite calcular a quantidade de cédulas necessárias para um determinado saque e oferece sugestão de valor máximo que pode ser sacado quando o valor solicitado não pode ser completamente atendido com as cédulas disponíveis.

### Dificuldades Encontradas

Durante o desenvolvimento deste projeto, uma das principais dificuldades encontradas foi relacionada ao teste no CMD devido a um conflito entre os dois SSDs do meu notebook. Isso impactou o processo de teste, exigindo ajustes na forma como o ambiente era configurado.

### Como Executar o Projeto

#### Pré-requisitos

- Python 3 instalado


#### Clone o repositório

Clone este repositório: https://github.com/wellingtonpvs/Desafio-Processo-Seletivo-Engenheiro-de-Software-Estagio-

### No CMD
1. Instale o Flask utilizando o seguinte comando no terminal:  pip install flask
2. Instale as dependências: pip install -r requirements.txt


#### Executando a Aplicação

3. Para iniciar o servidor Flask: python caixaEletronico.py (é importante estar no mesmo diretório do aruqivo para conseguir executar. Exemplo: C:\Users\welli\Projetos>(onde está armazenado o arquivo caixaEletronico.py))  

#### Testando a API
4. Após iniciar o servidor Flask, abra uma nova janela do terminal(CMD) e utilize o seguinte comando: 
curl -X POST -H "Content-Type: application/json" -d "{"valor": 150}" http://localhost:5000/api/saque

 Exemplo de resposta esperada(caso seja inserido um valor aceito):

    {
       "100": 1,
       "50": 1,
       "20": 0,
       "10": 0,
       "5": 0,
       "2": 0
    }

Exemplo de resposta esperada(caso seja inserido um valor que as notas não atendem):

    {
      "error": "Valor solicitado não pode ser atendido com as cédulas disponíveis",
      "sugestao de valor": 150
    }



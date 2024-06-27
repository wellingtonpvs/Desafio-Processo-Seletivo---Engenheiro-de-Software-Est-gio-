from flask import Flask, request, jsonify

caixaEletronico = Flask(__name__)

# Lista das cédulas disponíveis em ordem decrescente
cedulas = [100, 50, 20, 10, 5, 2]

@caixaEletronico.route('/api/saque', methods=['POST'])
def saque():
    data = request.get_json()
    
    # Validação de entrada
    if not data or 'valor' not in data:
        return jsonify({'error': 'Valor não fornecido'}), 400
    
    valor = data['valor']
    
    if not isinstance(valor, int) or valor <= 0:
        return jsonify({'error': 'O valor deve ser um número inteiro positivo'}), 400
    
    # Algoritmo para calcular a quantidade de cédulas
    resultado = {}
    valor_restante = valor
    
    for cedula in cedulas:
        quantidade = valor_restante // cedula
        resultado[str(cedula)] = quantidade
        valor_restante -= quantidade * cedula
    
    # Verificar se o valor solicitado pode ser atendido com as cédulas disponíveis
    if valor_restante > 0:
        sugestao = valor - valor_restante
        return jsonify({
            'error': 'Valor solicitado nao pode ser atendido com as cedulas disponiveis',
            'sugestao de valor': sugestao
        }), 400
    
    return jsonify(resultado)

if __name__ == '__main__':
    caixaEletronico.run(debug=True)

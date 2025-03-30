from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv('C:/Portfolio/TesteDeNivelamento/Tasks/banco_de_dados/files/processed_data/processed_Relatorio_cadop.csv',
                 sep = ';')
print(df['Cidade'].head())

@app.route('/buscar', methods=['GET'])
def buscar_operadora():
    try:
        termo = request.args.get('termo', '')
        print(f"Termo recebido: {termo}")
        
        if not termo:
            return jsonify({"erro": "Nenhum termo fornecido"}), 400
        
        if 'Cidade' not in df.columns:
            return jsonify({"erro": "Coluna 'Cidade' não encontrada no CSV"}), 500
        
        print(f"Iniciando busca por {termo}")
        print(f'tipo do termo: {type(termo)}')
        resultados = df[df['Cidade'].str.contains(termo, case=False, na=False)]
        print(f"Resultados encontrados: {len(resultados)}")

        return jsonify(resultados.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

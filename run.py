"""
Arquivo de entrada para iniciar a aplicação
"""
import os
import sys

# Verificar que estamos no diretório correto
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

if __name__ == "__main__":
    # Importar e executar a função principal
    from src.main import main
    main() 
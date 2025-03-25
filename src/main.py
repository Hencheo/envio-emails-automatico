"""
Arquivo principal para iniciar a aplicação
"""
import sys
import os
import traceback
from tkinter import messagebox

# Adicionar o diretório pai ao path para importações
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar a janela principal
from src.ui.main_window import MainWindow


def handle_exception(exc_type, exc_value, exc_traceback):
    """Manipula exceções não tratadas"""
    # Formatar o erro
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    
    # Registrar o erro em um arquivo de log
    try:
        os.makedirs("logs", exist_ok=True)
        with open("logs/error.log", "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(error_msg)
    except:
        pass
    
    # Exibir mensagem de erro
    messagebox.showerror(
        "Erro Inesperado",
        f"Ocorreu um erro inesperado na aplicação:\n\n{str(exc_value)}\n\n"
        f"Detalhes foram salvos em logs/error.log"
    )


def main():
    """Função principal para iniciar a aplicação"""
    # Configurar manipulador de exceções
    sys.excepthook = handle_exception
    
    try:
        # Criar e iniciar a janela principal
        app = MainWindow()
        app.run()
    except Exception as e:
        # Capturar qualquer exceção não tratada
        handle_exception(type(e), e, e.__traceback__)


if __name__ == "__main__":
    main()
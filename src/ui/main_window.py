"""
Janela principal da aplicação
"""
import os
import sys
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Configuração global do customtkinter
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MainWindow:
    """Classe principal da interface gráfica"""
    
    def __init__(self):
        """Inicializa a janela principal"""
        self.root = ctk.CTk()
        self.root.title("Sistema de Envio de E-mails")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Definir o ícone da aplicação se disponível
        try:
            if getattr(sys, 'frozen', False):
                # Executando como aplicativo congelado
                application_path = os.path.dirname(sys.executable)
            else:
                application_path = os.path.dirname(os.path.abspath(__file__))
                
            icon_path = os.path.join(application_path, "assets", "icon.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception:
            pass  # Ignorar erros de ícone
        
        # Criar conteúdo principal
        self._create_tabs()
        
    def _create_tabs(self):
        """Cria o sistema de abas da aplicação"""
        # Criar o notebook (sistema de abas)
        self.tabview = ctk.CTkTabview(self.root)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Adicionar as abas
        self.tab_emails = self.tabview.add("Lista de E-mails")
        self.tab_config = self.tabview.add("Configurações")
        self.tab_attachments = self.tabview.add("Anexos")
        self.tab_send = self.tabview.add("Envio")
        
        # Criar o conteúdo de cada aba
        # Nota: Na implementação real, cada aba seria uma classe separada
        self._setup_email_list_tab()
        self._setup_config_tab()
        self._setup_attachments_tab()
        self._setup_send_tab()
    
    def _setup_email_list_tab(self):
        """Configura a aba de lista de emails"""
        # Este é apenas um placeholder
        ctk.CTkLabel(self.tab_emails, 
                     text="Aqui será implementada a lista de e-mails").pack(pady=20)
    
    def _setup_config_tab(self):
        """Configura a aba de configurações"""
        # Este é apenas um placeholder
        ctk.CTkLabel(self.tab_config, 
                     text="Aqui serão implementadas as configurações").pack(pady=20)
    
    def _setup_attachments_tab(self):
        """Configura a aba de anexos"""
        # Este é apenas um placeholder
        ctk.CTkLabel(self.tab_attachments, 
                     text="Aqui será implementado o gerenciamento de anexos").pack(pady=20)
    
    def _setup_send_tab(self):
        """Configura a aba de envio"""
        # Este é apenas um placeholder
        ctk.CTkLabel(self.tab_send, 
                     text="Aqui será implementada a interface de envio").pack(pady=20)
    
    def run(self):
        """Inicia o loop principal da interface"""
        self.root.mainloop()


# Teste direto do módulo
if __name__ == "__main__":
    app = MainWindow()
    app.run()
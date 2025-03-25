"""
Aba de envio de e-mails
"""
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk


class SendTab:
    """Aba de envio de e-mails"""
    
    def __init__(self, parent):
        """
        Inicializa a aba de envio
        
        Args:
            parent: Widget pai (frame/tab)
        """
        self.parent = parent
        self.is_sending = False
        
        self._create_widgets()
        self._setup_layout()
    
    def _create_widgets(self):
        """Cria os widgets da aba"""
        # Frame de conteúdo
        self.content_frame = ctk.CTkFrame(self.parent)
        
        # Assunto
        self.subject_label = ctk.CTkLabel(self.content_frame, text="Assunto:")
        self.subject_entry = ctk.CTkEntry(self.content_frame, width=400)
        
        # Corpo da mensagem
        self.message_label = ctk.CTkLabel(self.content_frame, text="Mensagem:")
        self.message_text = ctk.CTkTextbox(self.content_frame, width=600, height=300)
        
        # Opções de formato
        self.html_var = tk.BooleanVar(value=False)
        self.html_check = ctk.CTkCheckBox(
            self.content_frame, 
            text="Usar HTML", 
            variable=self.html_var,
            onvalue=True,
            offvalue=False
        )
        
        # Botões
        self.button_frame = ctk.CTkFrame(self.content_frame)
        self.send_button = ctk.CTkButton(
            self.button_frame, 
            text="Enviar E-mails",
            command=self._on_send
        )
        self.stop_button = ctk.CTkButton(
            self.button_frame, 
            text="Parar Envio",
            command=self._on_stop,
            fg_color="#bf4040",
            hover_color="#8B0000"
        )
        self.stop_button.configure(state="disabled")
        
        # Log de envio
        self.log_label = ctk.CTkLabel(self.content_frame, text="Log de envio:")
        self.log_text = ctk.CTkTextbox(self.content_frame, width=600, height=150)
        self.log_text.configure(state="disabled")
        
    def _setup_layout(self):
        """Organiza o layout dos widgets"""
        # Frame principal
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Assunto
        self.subject_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.subject_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        # Corpo da mensagem
        self.message_label.grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        self.message_text.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        # Opções de formato
        self.html_check.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        
        # Botões
        self.button_frame.grid(row=3, column=1, sticky="ew", padx=5, pady=10)
        self.send_button.pack(side="left", padx=5)
        self.stop_button.pack(side="left", padx=5)
        
        # Log de envio
        self.log_label.grid(row=4, column=0, sticky="nw", padx=5, pady=5)
        self.log_text.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        
        # Configurar expansão
        self.content_frame.columnconfigure(1, weight=1)
        
    def _on_send(self):
        """Manipula o evento de clique no botão de envio"""
        if self.is_sending:
            return
        
        # Exemplo simplificado - a implementação real seria mais complexa
        subject = self.subject_entry.get().strip()
        message = self.message_text.get("1.0", "end").strip()
        
        if not subject:
            messagebox.showerror("Erro", "O assunto não pode estar vazio.")
            return
        
        if not message:
            messagebox.showerror("Erro", "A mensagem não pode estar vazia.")
            return
        
        # Aqui seria implementada a lógica real de envio
        self._add_to_log("Iniciando envio de e-mails...")
        self._add_to_log("Esta é apenas uma simulação da aba de envio.")
        
        # Atualizar estado da interface
        self.is_sending = True
        self.send_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
    
    def _on_stop(self):
        """Manipula o evento de clique no botão de parar envio"""
        if not self.is_sending:
            return
        
        # Aqui seria implementada a lógica real de parada
        self._add_to_log("Parando envio de e-mails...")
        
        # Atualizar estado da interface
        self.is_sending = False
        self.send_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
    
    def _add_to_log(self, message):
        """Adiciona uma mensagem ao log de envio"""
        self.log_text.configure(state="normal")
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
        
        # Atualizar a interface
        self.parent.update()
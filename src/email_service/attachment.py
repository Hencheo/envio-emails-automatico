"""
Módulo para manipulação de anexos de e-mail
"""
import os
import mimetypes
from typing import Dict, Optional, Union


class Attachment:
    """Classe para representar um anexo de e-mail"""
    
    def __init__(self, file_path: str, custom_name: Optional[str] = None):
        """
        Inicializa um anexo
        
        Args:
            file_path: Caminho para o arquivo
            custom_name: Nome personalizado para o anexo (opcional)
        
        Raises:
            FileNotFoundError: Se o arquivo não existir
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
            
        self.file_path = os.path.abspath(file_path)
        self.original_name = os.path.basename(file_path)
        self.custom_name = custom_name
        
        # Determinar o tipo MIME do arquivo
        mime_type, encoding = mimetypes.guess_type(file_path)
        self.mime_type = mime_type or "application/octet-stream"
        
        # Obter o tamanho do arquivo
        self.size = os.path.getsize(file_path)
    
    @property
    def name(self) -> str:
        """Retorna o nome do anexo a ser exibido"""
        return self.custom_name or self.original_name
    
    @property
    def size_formatted(self) -> str:
        """Retorna o tamanho do arquivo formatado para exibição"""
        # Converter para KB
        size_kb = self.size / 1024
        
        if size_kb < 1024:
            return f"{size_kb:.1f} KB"
        else:
            # Converter para MB
            size_mb = size_kb / 1024
            return f"{size_mb:.1f} MB"
    
    def get_content(self) -> bytes:
        """
        Lê e retorna o conteúdo do arquivo
        
        Returns:
            Conteúdo do arquivo em bytes
        """
        with open(self.file_path, "rb") as f:
            return f.read()
    
    def to_dict(self) -> Dict[str, Union[str, int]]:
        """
        Converte o anexo para um dicionário
        
        Returns:
            Dicionário com os dados do anexo
        """
        return {
            "file_path": self.file_path,
            "name": self.name,
            "original_name": self.original_name,
            "custom_name": self.custom_name,
            "mime_type": self.mime_type,
            "size": self.size,
            "size_formatted": self.size_formatted
        }
    
    def __eq__(self, other) -> bool:
        """
        Verifica se dois anexos são iguais
        
        Args:
            other: Outro objeto para comparação
            
        Returns:
            True se os anexos são iguais, False caso contrário
        """
        if not isinstance(other, Attachment):
            return False
        
        return self.file_path == other.file_path
    
    def __str__(self) -> str:
        """
        Representação em string do anexo
        
        Returns:
            String formatada com os dados do anexo
        """
        return f"{self.name} ({self.size_formatted})"
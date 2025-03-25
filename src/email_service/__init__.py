"""
Pacote para serviços de email
"""

# Exportar classes principais
from src.email_service.sender_manager import SenderManager
from src.email_service.attachment import Attachment

__all__ = [
    'SenderManager',
    'Attachment',
]
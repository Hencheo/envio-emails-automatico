"""
Pacote de interface de usuário
"""

# Importar componentes principais da UI para facilitar importações
from src.ui.main_window import MainWindow
from src.ui.email_list_tab import EmailListTab
from src.ui.smtp_tab import SmtpTab
from src.ui.attachment_tab import AttachmentTab
from src.ui.send_tab import SendTab

__all__ = [
    'MainWindow',
    'EmailListTab',
    'SmtpTab',
    'AttachmentTab',
    'SendTab',
]
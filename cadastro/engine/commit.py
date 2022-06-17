"""
Este módulo contém uma função para aplicar 'commit' no banco de dados.
"""
import sqlite3
database = r'.\enderecos.db'

def commit():
    """
    Essa função irá 'commitar' as mudanças que forem efetuadas no banco de dados.
    """
    connector = sqlite3.connect(database)
    connector.commit()
    connector.close()

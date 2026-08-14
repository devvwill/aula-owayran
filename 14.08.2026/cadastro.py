def normalizar_cpf (cpf: str) -> str:   
    return re.sub(r"\D", "'", cpf)

def validar_cpf (cpf:str) -> bool:
    return len (cpf) == 11 and cpf.isdigit()

def cadastrar_cliente (cpf:str ) -> Cliente: 
    cpf = normalizar_cpf (cpf) 
    if not validar_cpf(cpf):
        raise ValueError ("CPF inválido")
    return salvar_cleinte (cpf)
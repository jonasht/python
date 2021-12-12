from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len (documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('quantidade de digitos esta incorreto')

class DocCpf:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError('cpf invalido')

    def __str__(self) -> str:
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.documento)
    
class DocCnpj:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError('cnpj invalido')
    
    def __str__(self):
        return self.format()
        
    def valida(self, documento):
        mascara = CNPJ()
        return mascara.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)
    
class CpfCnpj:
    def __init__(self, documento, tipo_documento) -> None:
        self.tipo_documento = tipo_documento
        # self.cpf = ''
        # self.cnpj = ''

        documento = str(documento)
        if self.tipo_documento == 'cpf':
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('cpf invalido')
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('cnpj invalido')
        else:
            raise ValueError('tipo de documento invalido')
                

    def __str__(self) -> str:
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        else:
            return self.format_cnpj()
            
    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError('quantidade de digitos invalido')
    
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError('quantidos de digitos invalidos')

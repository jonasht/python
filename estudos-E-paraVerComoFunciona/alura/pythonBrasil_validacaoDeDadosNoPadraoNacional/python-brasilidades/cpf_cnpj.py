from validate_docbr import CPF, CNPJ


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

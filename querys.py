class Querys:
    @staticmethod
    def query_1(ref):
        return f"""
        SELECT *
        FROM sua_tabela
        WHERE mes_referencia = '{ref}'
        """

    @staticmethod
    def query_2(ref):
        return f"""
        SELECT *
        FROM outra_tabela
        WHERE mes_referencia = '{ref}'
        """


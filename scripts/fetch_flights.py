# Remove duplicatas internas antes do envio
# (a API SIROS pode retornar o mesmo voo mais de uma vez)
def deduplicar(lista: list) -> list:
    seen = set()
    result = []
    for r in lista:
        key = (
            r.get("data_referencia"),
            r.get("icao_empresa"),
            r.get("numero_voo"),
            r.get("icao_origem"),
            r.get("icao_destino"),
            r.get("etapa"),
        )
        if key not in seen:
            seen.add(key)
            result.append(r)
    return result

antes = len(registros)
registros = deduplicar(registros)
removidos = antes - len(registros)
if removidos:
    print(f"  Deduplicação: {removidos} registro(s) duplicado(s) removido(s) antes do envio")

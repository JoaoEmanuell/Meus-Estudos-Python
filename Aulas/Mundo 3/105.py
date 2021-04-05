def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        if r['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'ruim'
    return r


resp = notas(6.0, 5.6, 4.3, 6.9, sit=True)
print(resp)

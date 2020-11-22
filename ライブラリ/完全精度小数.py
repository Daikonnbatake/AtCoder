def decimal(s): #str型の小数を入力
    dotindex=list(s).index('.')
    s=s[:dotindex]+s[dotindex+1:]
    return s
print(decimal('989.0008'))
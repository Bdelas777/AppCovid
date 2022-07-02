def aguinaldo(sal,respuesta):
	dias=float(input("Cuantos dias le pagara "))
	meses=int(input("Cuantos meses trabajo "))
	if respuesta=="m" or respuesta=="M":
		sal=sal/30.4
		sal=round(sal,2)
		sal=sal*dias
		sal=sal*meses
		sal=sal/12
		sal=round(sal,2)
		return sal
	if respuesta=="q" or respuesta=="Q":
		sal=sal/14
		sal=round(sal,2)
		sal=sal*dias
		sal=sal*meses
		sal=sal/12
		sal=round(sal,2)
		return sal
	if respuesta=="s" or respuesta=="S":
		sal=sal/7
		sal=round(sal,2)
		sal=sal*dias
		sal=sal*meses
		sal=sal/12
		sal=round(sal,2)
		return sal

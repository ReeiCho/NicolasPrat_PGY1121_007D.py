import funciones as fn

fn.mostrar_menu()
opcion=fn.validar_opcion()
if opcion == 1:
    fn.comprar_departamento()
    fn.validar_piso()
    fn.precios_deptos()
    fn.validar_tipo_depto()
    fn.validar_rut()
    
elif opcion == 2:
    fn.mostrar_departamentos()
    
elif opcion == 3:
    print(fn.lista_rut)
    fn.time.sleep(3)
elif opcion == 4:
    fn.ventas_totales()
else:
    fn.mensaje_salida()



def build_user(request):
    user = {
        'pasaporte': request.POST['pasaporte'],
        'rut': request.POST['rut'],
        'dv': request.POST['dv'],
        'primerNombre': request.POST['primerNombre'],
        'segundoNombre': request.POST['segundoNombre'],
        'apellidoPaterno': request.POST['primerApellido'],
        'apellidoMaterno': request.POST['segundoApellido'],
        'fechaNacimiento': request.POST['fechaNacimiento'],
        'correo': request.POST['correo'],
        'telefonoMovil': request.POST['telefonoMovil'],
        'telefonoFijo': request.POST['telefonoFijo'],
        'password': request.POST['hashedPassword'],
        'genero': request.POST['genero'],
        'pais': request.POST['pais'],
        'tipoUsuario': request.POST['tipoUsuario'],
        'direccion': {
            'comuna': request.POST['comuna'],
            'calle': request.POST['calle'],
            'numero': request.POST['numero'],
            'depto': request.POST['depto'],
            'casa': request.POST['casa']
        }
    }
    return user
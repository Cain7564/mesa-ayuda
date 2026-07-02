const guardarUsuario = async (datos) => {

    console.log("===== DATOS ENVIADOS =====")
    console.log(datos)

    try {

        // Copia de los datos
        const datosEnviar = { ...datos }

        // Si estamos editando y la contraseña está vacía,
        // no la enviamos al backend.
        if (
            usuarioSeleccionado.value &&
            (!datosEnviar.password || datosEnviar.password.trim() === '')
        ) {

            delete datosEnviar.password

        }

        if (usuarioSeleccionado.value) {

            await updateUser(
                usuarioSeleccionado.value.id,
                datosEnviar
            )

            alert("Usuario actualizado correctamente.")

        } else {

            await createUser(datosEnviar)

            alert("Usuario creado correctamente.")

        }

        cerrarModal()

        await cargarUsuarios()

    } catch (error) {

        console.log("===== ERROR =====")

        console.log(error)

        if (error.response) {

            console.log(error.response.data)

            alert(
                JSON.stringify(
                    error.response.data,
                    null,
                    2
                )
            )

        }

    }

}
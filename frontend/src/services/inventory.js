import api from './api'

export const getEquipos = async (

    page = 1,

    tipo = '',

    estado = '',

    search = '',

    ordering = ''

) => {

    let url = `equipos/?page=${page}`

    if (tipo) {

        url += `&tipo=${tipo}`

    }

    if (estado) {

        url += `&estado=${estado}`

    }

    if (search) {

        url += `&search=${search}`

    }

    if (ordering) {

        url += `&ordering=${ordering}`

    }

    const response = await api.get(url)

    return response.data

}

export const createEquipo = async (data) => {

    const response = await api.post(

        'equipos/',

        data

    )

    return response.data

}

export const updateEquipo = async (id, data) => {

    const response = await api.put(

        `equipos/${id}/`,

        data

    )

    return response.data

}

export const deleteEquipo = async (id) => {

    await api.delete(

        `equipos/${id}/`

    )

}

export const getMarcas = async () => {

    const response = await api.get(

        'marcas/'

    )

    return response.data

}

export const getSistemasOperativos = async () => {

    const response = await api.get(

        'sistemas-operativos/'

    )

    return response.data

}

export const getUbicaciones = async () => {

    const response = await api.get(

        'ubicaciones/'

    )

    return response.data

}

export const getEstadosEquipo = async () => {

    const response = await api.get(

        'estados-equipo/'

    )

    return response.data

}
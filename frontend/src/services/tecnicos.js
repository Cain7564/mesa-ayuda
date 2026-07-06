import api from './api'

export const getTecnicos = async (

    page = 1,

    search = '',

    ordering = ''

) => {

    let url = `users/tecnicos/?page=${page}`

    if (search) {

        url += `&search=${search}`

    }

    if (ordering) {

        url += `&ordering=${ordering}`

    }

    const response = await api.get(url)

    return response.data

}

export const createTecnico = async (data) => {

    const response = await api.post(

        'users/tecnicos/',

        data

    )

    return response.data

}

export const updateTecnico = async (id, data) => {

    const response = await api.put(

        `users/tecnicos/${id}/`,

        data

    )

    return response.data

}

export const deleteTecnico = async (id) => {

    await api.delete(

        `users/tecnicos/${id}/`

    )

}
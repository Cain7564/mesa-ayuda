import api from './api'

const getAuthHeaders = () => {

    const token = localStorage.getItem('access')

    return {

        Authorization: `Bearer ${token}`

    }

}

export const getUsers = async (

    page = 1,

    rol = '',

    search = '',

    ordering = ''

) => {

    let url = `users/?page=${page}`

    if (rol) {

        url += `&rol=${rol}`

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

export const createUser = async (userData) => {

    const response = await api.post(

        'users/',

        userData,

        {

            headers: getAuthHeaders()

        }

    )

    return response.data

}

export const updateUser = async (id, userData) => {

    const response = await api.put(

        `users/${id}/`,

        userData,

        {

            headers: getAuthHeaders()

        }

    )

    return response.data

}

export const deleteUser = async (id) => {

    await api.delete(

        `users/${id}/`,

        {

            headers: getAuthHeaders()

        }

    )

}

export const getUsuariosSimple = async () => {

    const response = await api.get(

        'users/simple/'

    )

    return response.data

}

export const getTecnicosSimple = async () => {

    const response = await api.get(

        'users/tecnicos/simple/'

    )

    return response.data

}
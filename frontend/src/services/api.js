import api from './api'

export const getUsers = async (page = 1, rol = '') => {

    let url = `users/?page=${page}`

    if (rol) {

        url += `&rol=${rol}`

    }

    const response = await api.get(url)

    return response.data

}

export const createUser = async (userData) => {

    const response = await api.post(

        'users/',

        userData

    )

    return response.data

}

export const updateUser = async (id, userData) => {

    const response = await api.put(

        `users/${id}/`,

        userData

    )

    return response.data

}

export const deleteUser = async (id) => {

    await api.delete(

        `users/${id}/`

    )

}
import api from './api'

const getAuthHeaders = () => {

    const token = localStorage.getItem('access')

    return {

        Authorization: `Bearer ${token}`

    }

}

export const getUsers = async () => {

    const response = await api.get('users/', {

        headers: getAuthHeaders()

    })

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
import api from './api'

export const getTickets = async (

    page = 1,

    estado = '',

    prioridad = '',

    search = '',

    ordering = ''

) => {

    let url = `tickets/?page=${page}`

    if (estado) {

        url += `&estado=${estado}`

    }

    if (prioridad) {

        url += `&prioridad=${prioridad}`

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

export const createTicket = async (ticketData) => {

    const response = await api.post(

        'tickets/',

        ticketData

    )

    return response.data

}

export const updateTicket = async (id, ticketData) => {

    const response = await api.put(

        `tickets/${id}/`,

        ticketData

    )

    return response.data

}

export const deleteTicket = async (id) => {

    await api.delete(

        `tickets/${id}/`

    )

}
export const getCategoriasSimple = async () => {

    const response = await api.get(

        'categorias/simple/'

    )

    return response.data

}
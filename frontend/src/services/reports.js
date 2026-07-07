import api from './api'

export const getReporteGeneral = async () => {

    const response = await api.get(

        'reports/general/'

    )

    return response.data

}
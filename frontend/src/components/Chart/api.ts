import axios from "axios";

export interface Coords {
    x: Date
    y: number
}

export interface ChartResponse {
    data: Coords[],
    meta: {
        total: number
    }
}

export const getData = async () =>
    axios.get<ChartResponse>(`${process.env.REACT_APP_API_URL!}/orders/chart`).then(res => res.data)
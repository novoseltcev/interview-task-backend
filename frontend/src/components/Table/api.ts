import axios from "axios";

export interface Order extends Object{
    id: number
    num_order: number
    delivery_date: Date
    rubble_cost: string
}

export interface OrdersResponse {
    data: Order[],
    meta: {
        pages: number
    }
}

export const getPage = async (page: number) =>
    axios.get<OrdersResponse>(`${process.env.REACT_APP_API_URL!}/orders?page=${page}`).then(res => res.data)

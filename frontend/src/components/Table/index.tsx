import React, {ChangeEvent, FC, useEffect, useState} from 'react';
import {Table as MUITable, TableBody, TableCell, TableHead, TableRow, Pagination} from "@mui/material";

import styles from './index.module.css';
import {getPage, Order} from './api';

const Table: FC = () => {
    const headerNames = ['№', 'заказ №', 'стоимость, ₽', 'срок поставки'];

    const [data, setData] = useState<Order[]>([]);
    const [page, setPage] = useState<number>(1);
    const [countPages, setCountPages] = useState<number>(1);
    const [isLoading, setIsLoading] = useState<boolean>(true)

    useEffect(() => {
        getPage(page)
            .then(data => {
                setData(data.data)
                setCountPages(data.meta.pages)
            })
            .catch(err => console.log(err))
            .finally(() => setIsLoading(false))
    }, [page])

    const getOrderFieldByName = (row: Order) => {
        return <TableRow key={row.id}>
            <TableCell>{row.id}</TableCell>
            <TableCell>{row.num_order}</TableCell>
            <TableCell>{parseFloat(row.rubble_cost).toFixed(2)}</TableCell>
            <TableCell>{row.delivery_date.toString()}</TableCell>
        </TableRow>
    }

    return (
        <div>
            {isLoading
                ? "Загрузка"
                : <div>
                    <MUITable>
                        <TableHead>
                            <TableRow>
                                {headerNames.map((name) => (
                                    <TableCell variant="head" key={name}>
                                        {name}
                                    </TableCell>
                                ))}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {data.map((row: Order) => getOrderFieldByName(row))}
                        </TableBody>
                    </MUITable>
                    <Pagination className={styles.pagination} count={countPages} shape="rounded" onChange={(e, page) => setPage(page)}/>
                </div>
            }
        </div>
    );
}

export default Table;
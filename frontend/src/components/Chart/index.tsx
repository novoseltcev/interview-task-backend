import React, {useEffect, useState} from 'react';
import {
    ArcElement,
    CategoryScale,
    Chart as ChartJS,
    Legend,
    LinearScale,
    LineElement,
    PointElement,
    Title,
    Tooltip,
} from "chart.js";
import {Line} from 'react-chartjs-2';

import {Coords, getData} from './api';
import styles from './index.module.css';

ChartJS.register(
    ArcElement,
    Tooltip,
    Legend,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title
);

const Chart = () => {
    const [data, setData] = useState<Coords[]>([]);
    const [total, setTotal] = useState<number>(0);
    const [isLoading, setIsLoading] = useState<boolean>(true)

    useEffect(() => {
        getData()
            .then(data => {
                setData(data.data)
                setTotal(data.meta.total)
            })
            .catch(err => console.log(err))
            .finally(() => setIsLoading(false))
    }, [])

    const chartData = {
        labels: data.map((coords: Coords) => coords.x),
        datasets: [{
            label: 'Изменение суммарной стоимости поставок по дням',
            data: data.map((coords: Coords) => coords.y),
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    };

    return <div>
        {
            isLoading ? <p>Загрузка</p> : (
                <>
                    <div className={styles.total}>
                        <p>Общая сумма поставок</p>
                        <p>{parseFloat(String(total)).toFixed(2)} ₽</p>
                    </div>
                    <Line data={chartData}></Line>
                </>
            )
        }
    </div>
};

export default Chart;
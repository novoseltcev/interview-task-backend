import React from 'react';

import styles from './App.module.css';
import Header from "./components/Header";
import Chart from "./components/Chart";
import Table from "./components/Table";

export default function App() {
    return (
        <div className={styles.App}>
            <Header />
            <div className={styles.container}>
                <Chart/>
                <Table/>
            </div>
        </div>
    );
}
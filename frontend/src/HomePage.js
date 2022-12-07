import React, { useState, useEffect } from 'react'
import Table from 'react-bootstrap/Table';
import axios from 'axios';


const HomePage = () => {

    const [tableData, setTableData] = useState([])
    const [counter, setCounter] = useState(3)
    const [counterStatus, setCounterStatus] = useState(true)

    // useState(() => {
    //     if (counter > 5) {
    //         setCounter(0)
    //     }
    // }, [counter])

    const getNewRecords = async () => {
        setCounterStatus(false)
        let headers = {
            'type': 'application/json'
        }

        // new records request
        const fetchDataRequest = await axios.post('http://127.0.0.1:8000/api/v1/', headers = headers)

        if (fetchDataRequest.status === 200) {

            // fetch new records
            const axiosResponse = await axios.get('http://127.0.0.1:8000/api/v1/', headers = headers)
            console.log("data response =>", axiosResponse)
            setTableData(axiosResponse.data)
        }
        setCounterStatus(true)
    }

    useEffect(() => {
        if (counterStatus) {
            setTimeout(() => {
                if (counter === 0) {
                    setCounter(3)
                    getNewRecords()
                } else {
                    setCounter(counter - 1)
                }
            }, 1000)
        }
    }, [counter, counterStatus])


    // console.log("Table data =>", tableData)

    return (
        <div>
            <div style={{ textAlign: "center" }}>
                <h3>{"Cryptocurrency Prices by Market Cap"}</h3>
            </div>

            <p>
                <span style={{ fontSize: "12px"}}>
                <b>Note:</b> The website from which below data is scrapped from is not providing any realtime records, its
                just few addition and subtraction of values they are doing with the data to keep user engaged,
                try refreshing the website <a href="https://coinmarketcap.com/">https://coinmarketcap.com/</a> you will find the values matching 
                with below table values. Means, on the coinmarket website the data is getting fetched after fews minutes not instantly. Therefore it could
                happen that even in 5 seconds you will notice no change in the table below.
                </span>
            </p>

            {/* <div><button onClick={getNewRecords}>Get records</button></div> */}

            <p><span style={{ color: "purple", fontWeight: "bold" }}>{`Refreshing records in ${counter}`}</span></p>

            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>{"S.No"}</th>
                        <th>{"Name"}</th>
                        <th>{"Price"}</th>
                        <th>{"1h %"}</th>
                        <th>{"24h %"}</th>
                        <th>{"7d %"}</th>
                        <th>{"Market Cap"}</th>
                        <th>{"Volume(24h)"}</th>
                        <th>{"Circulating Supply"}</th>
                    </tr>
                </thead>
                <tbody>
                    {tableData ? tableData.map((each_obj, idx) => (
                        <tr key={idx}>
                            <td>
                                {idx + 1}
                            </td>
                            <td>
                                {each_obj ? each_obj.name : "-"}
                            </td>
                            <td>
                                {"$"}{each_obj ? each_obj.price : "-"}
                            </td>
                            <td>
                                {each_obj ? each_obj.perhour : "-"}{"%"}
                            </td>
                            <td>
                                {each_obj ? each_obj.day : "-"}{"%"}
                            </td>
                            <td>
                                {each_obj ? each_obj.week : "-"}{"%"}
                            </td>
                            <td>
                                {"$"}{each_obj ? each_obj.marketcap : "-"}
                            </td>
                            <td>
                                {"$"}{each_obj ? each_obj.volume : "-"}
                            </td>
                            <td>
                                {each_obj ? each_obj.cirulating_supply : "-"}
                            </td>
                        </tr>
                    )) : null}

                </tbody>
            </Table>
        </div>
    )
}

export default HomePage
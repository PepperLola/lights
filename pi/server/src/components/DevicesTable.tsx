import React, { useEffect, useState } from 'react';
import { Table } from 'antd';
import type { ColumnsType, TableProps } from 'antd/es/table';

interface DataType {
    key: React.Key;
    name: string;
    port: number;
    length: number;
    effect?: string;
}

const columns: ColumnsType<DataType> = [
    {
        title: 'Name',
        dataIndex: 'name',
        sorter: (a, b) => a.name == b.name ? 0 : a.name < b.name ? 1 : -1,
    },
    {
        title: 'Port',
        dataIndex: 'port',
        sorter: (a, b) => a.port - b.port,
    },
    {
        title: 'Length',
        dataIndex: 'length',
        sorter: (a, b) => a.length - b.length,
    },
    {
        title: 'Effect',
        dataIndex: 'effect',
        sorter: (a, b) => a.name == b.name ? 0 : a.name < b.name ? 1 : -1,
    }
];

const onChange: TableProps<DataType>['onChange'] = (pagination, filters, sorter, extra) => {
    console.log('params', pagination, filters, sorter, extra);
};

const DevicesTable: React.FC = () => {
    const [data, setData] = useState<DataType[]>([]);

    useEffect(() => {
        fetch("http://localhost:2733/devices")
            .then(res => res.json())
            .then(( data: DataType[] ) => {
                data = data.map(d => ({...d, key: d.name }));
                setData(data);
            })
            .catch(console.error);
    }, []);

    return (
        <Table columns={columns} dataSource={data} onChange={onChange} />
    );
}

export default DevicesTable;

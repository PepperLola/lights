import React from 'react';
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
    const data: DataType[] = [
        {
            key: '1',
            name: 'Test Strip',
            port: 0,
            length: 64,
            effect: 'Rainbow',
        },
        {
            key: '2',
            name: 'abab',
            port: 1,
            length: 64,
            effect: 'Solid',
        },
        {
            key: '3',
            name: 'Test Strip 2',
            port: 2,
            length: 64,
            effect: 'Text',
        },
        {
            key: '4',
            name: 'Front Left Arm Strip',
            port: 3,
            length: 64,
            effect: 'Breathing',
        },
    ];

    return (
        <Table columns={columns} dataSource={data} onChange={onChange} />
    );
}

export default DevicesTable;

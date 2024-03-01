import { Typography, Upload, UploadFile, UploadProps, message } from "antd";
import {useState, useEffect} from 'react';

const CustomEffect = () => {
        const [previousEffects, setPreviousEffects] = useState<Array<UploadFile>>([]);

    useEffect(() => {
        fetch("http://localhost:2733/custom-effects")
            .then(res => res.json())
            .then(( json: string[] ) => setPreviousEffects(json.map((e: string, i: number) => ({uid: `${i}`, name: e, status: 'done'}))))
            .catch(e => console.error(e))
    }, [])

    const props: UploadProps = {
        name: 'file',
        action: 'http://localhost:2733/custom-effects',
        type: 'drag',
        listType: 'text',
        accept: '.py',
        onChange(info) {
            if (info.file.status !== 'uploading') {
                console.log(info.file, info.fileList);
            }
            setPreviousEffects(info.fileList)

            if (info.file.status === 'done') {
                message.success(`${info.file.name} file uploaded successfully!`);
            } else if (info.file.status === 'error') {
                message.error(`${info.file.name} file upload failed.`);
            }
        },
        onRemove(info) {
            if (info.name) {
                fetch(`http://localhost:2733/custom-effects?file=${info.name}`, { method: 'DELETE' });
            }
        }
    };

    return (
        <>
            <div>
                <Typography.Title>Custom Effect</Typography.Title>
                <Upload
                    style={{ height: "100px" }}
                    fileList={previousEffects}
                    {...props}
                />
            </div>
        </>
    );
}

export default CustomEffect;

import { Typography, Upload, UploadProps, message } from "antd";

const props: UploadProps = {
    name: 'file',
    action: 'http://localhost:2733/upload-effect',
    type: 'drag',
    listType: 'text',
    accept: '.py',
    onChange(info) {
        if (info.file.status !== 'uploading') {
            console.log(info.file, info.fileList);
        }
        if (info.file.status === 'done') {
            message.success(`${info.file.name} file uploaded successfully!`);
        } else if (info.file.status === 'error') {
            message.error(`${info.file.name} file upload failed.`);
        }
    }
};

const CustomEffect = () => {
    return (
        <>
            <div>
                <Typography.Title>Custom Effect</Typography.Title>
                <Upload
                    style={{ height: "100px" }}
                    {...props}
                />
            </div>
        </>
    );
}

export default CustomEffect;

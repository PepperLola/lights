import { Typography, Upload } from "antd";

const CustomEffect = () => {
    return (
        <>
            <div>
                <Typography.Title>Custom Effect</Typography.Title>
                <Upload name="Custom Effect" type="drag" listType="text" style={{ height: "100px" }} />
            </div>
        </>
    );
}

export default CustomEffect;

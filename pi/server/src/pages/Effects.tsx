import { List, Typography } from "antd";

const Effects = () => {
    const effects = [
        "Effect 1",
        "Effect 2",
        "Effect 3",
        "Effect 4",
    ]
    const custom_effects = [
        "Custom Effect 1",
        "Custom Effect 2",
        "Custom Effect 3",
        "Custom Effect 4"
    ]
    return (
        <>
            <Typography.Title>Effects</Typography.Title>
            <Typography.Text>Default</Typography.Text>
            <List bordered={true}>
                {effects.map(e => (<List.Item>{e}</List.Item>))}
            </List >
            <Typography.Text>Custom</Typography.Text>
            <List bordered={true}>
                {custom_effects.map(e => (<List.Item>{e}</List.Item>))}
            </List >
        </>
    );
}

export default Effects;

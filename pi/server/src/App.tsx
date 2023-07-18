import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import DefaultLayout from "./layout/default";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<DefaultLayout />}>
                    <Route index element={<Home />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App

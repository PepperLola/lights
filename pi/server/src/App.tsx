import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Effects from "./pages/Effects";
import DefaultLayout from "./layout/default";
import CustomEffect from "./pages/CustomEffect";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<DefaultLayout />}>
                    <Route index element={<Home />} />
                </Route>
                <Route path="/effects" element={<DefaultLayout />}>
                    <Route index element={<Effects />} />
                    <Route path="/effects/custom" element={<CustomEffect />} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
}

export default App

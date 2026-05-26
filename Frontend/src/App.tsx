import { Routes, Route, Link } from "react-router-dom";
import Products from "./pages/Products";
import Categories from "./pages/Categories";
import Dashboard from "./pages/Dashboard";
import Users from "./pages/Users";


function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      
      {/* NAVBAR SIMPLE */}
      <nav className="p-4 flex gap-4 bg-gray-800">
         <Link to="/">Dashboard</Link>
        <Link to="/products">Products</Link>
        <Link to="/categories">Categories</Link>
        <Link to="/users">Users</Link>
      </nav>

      {/* ROUTES */}
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/products" element={<Products />} />
        <Route path="/categories" element={<Categories />} />
        <Route path="/users" element={<Users />} />
      </Routes>

    </div>
  );

}

export default App;
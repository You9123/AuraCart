import { useEffect, useState } from "react";
import axios from "axios";

// 1. Interfaz basada exactamente en las claves del JsonResponse de tu Django
interface DashboardStats {
  total_categories: number;
  total_products: number;
  low_stock_products: number;
  total_users:number;
  total_admins:number;
  total_clients:number;
}

function Dashboard() {
  // Inicializamos el estado con los nuevos campos de AuraCart en 0
  const [stats, setStats] = useState<DashboardStats>({
    total_categories: 0,
    total_products: 0,
    low_stock_products: 0,
    total_users: 0,
    total_admins: 0,
    total_clients: 0,
  });

  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // CORREGIDO: Cambiado de /dashboard/stats/ a /dashboard-stats
    axios
       .get("http://127.0.0.1:8000/api/dashboard_stats/")
        .then((res) => {
            setStats(res.data);
            setLoading(false);
        })
      .catch((err) => {
        console.error("Error loading AuraCart Dashboard statistics:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="p-10 text-white bg-gray-900 min-h-screen flex items-center justify-center">
        <p className="text-xl animate-pulse">Loading dashboard statistics...</p>
      </div>
    );
  }

  return (
    <div className="p-10 text-white bg-gray-900 min-h-screen">
      {/* Encabezado del Dashboard de AuraCart */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2">AuraCart Dashboard</h1>
        <p className="text-gray-400">Welcome back. Here is your store's catalog overview.</p>
      </div>

      {/* Grid de tarjetas del dashboard */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-6">
        
        {/* Tarjeta: Total de Categorías */}
        <div className="bg-gray-800 p-6 rounded-xl border-l-4 border-blue-500 shadow-lg">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-sm font-medium uppercase tracking-wider text-gray-400">Total Categories</h3>
          </div>
          <p className="text-4xl font-bold">{stats.total_categories}</p>
        </div>

        {/* Tarjeta: Total de Productos */}
        <div className="bg-gray-800 p-6 rounded-xl border-l-4 border-purple-500 shadow-lg">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-sm font-medium uppercase tracking-wider text-gray-400">Total Products</h3>
          </div>
          <p className="text-4xl font-bold">{stats.total_products}</p>
        </div>

        {/* Tarjeta: Alerta de Bajo Inventario (Cambia a rojo si hay productos en riesgo) */}
        <div className={`p-6 rounded-xl border-l-4 shadow-lg transition-all ${
          stats.low_stock_products > 0 
            ? "bg-red-950/40 border-red-500 text-red-200" 
            : "bg-gray-800 border-gray-600 text-white"
        }`}>
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-sm font-medium uppercase tracking-wider text-gray-400">Low Stock Items</h3>
          </div>
          <p className="text-4xl font-bold">{stats.low_stock_products}</p>
          {stats.low_stock_products > 0 && (
            <p className="text-xs text-red-400 mt-2 font-semibold animate-pulse">
              Action required: Products have under 5 units!
            </p>
          )}
        </div>

        {/* Total users */}
        <div className="bg-gray-800 p-6 rounded-xl border-l-4 border-green-500 shadow-lg">

            <div className="flex justify-between items-center mb-4">

                <h3 className="text-sm font-medium uppercase tracking-wider text-gray-400">

                    Total Users

                </h3>

            </div>

            <p className="text-4xl font-bold">

                {stats.total_users}

            </p>

        </div>

        {/* Administrators */}
        <div className="bg-gray-800 p-6 rounded-xl border-l-4 border-red-500 shadow-lg">

            <div className="flex justify-between items-center mb-4">

                <h3 className="text-sm font-medium uppercase tracking-wider text-gray-400">

                    Administrators

                </h3>

        </div>

        <p className="text-4xl font-bold text-red-400">

            {stats.total_admins}

            </p>

        </div>

         {/* Clients */}

        <div className="bg-gray-800 p-6 rounded-xl border-l-4 border-cyan-500 shadow-lg">

        <div className="flex justify-between items-center mb-4">

        <h3 className="text-sm font-medium uppercase tracking-wider text-gray-400">

            Clients

        </h3>

    </div>

    <p className="text-4xl font-bold text-cyan-400">

        {stats.total_clients}

    </p>

</div>

      </div>
    </div>
  );
}

export default Dashboard;

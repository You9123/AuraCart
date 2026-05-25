import { useEffect, useState } from "react";
import axios from "axios";

// 1. Corregida la interfaz para que coincida exactamente con tu modelo de Django
interface Category {
  id: number;
  name: string;
}

function Categories() {
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState<boolean>(true); // Estado de carga opcional

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/categories/")
      .then((res) => {
        setCategories(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching categories:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-gray-900 text-white">
        <p className="text-xl animate-pulse">Loading categories...</p>
      </div>
    );
  }

  return (
    <div className="p-10 text-white bg-gray-900 min-h-screen">
      <h1 className="text-4xl font-bold mb-6">Categories</h1>

      <div className="space-y-4">
        {categories.length === 0 ? (
          <p className="text-gray-400 italic">No categories found. Add some in Django Admin!</p>
        ) : (
          categories.map((c) => (
            <div 
              key={c.id} 
              className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-md flex justify-between items-center transition-all hover:border-blue-500/50"
            >
              
              {/* Información de la Categoría (Izquierda) */}
              <div className="space-y-1">
                <h2 className="text-2xl font-semibold text-blue-400">{c.name}</h2>
                <p className="text-gray-400 text-sm">
                  System ID: <span className="text-gray-200 font-mono">#{c.id}</span>
                </p>
              </div>

              {/* Tarjeta lateral de la Categoría (Derecha) - Adaptada a los datos reales */}
              <div className="bg-gray-700/60 p-4 rounded-xl border border-gray-600 w-64 min-h-[90px] flex flex-col justify-center shadow-inner">
                <span className="text-xs font-bold uppercase tracking-widest text-gray-400 block mb-1">
                  AuraCart Section
                </span>
                <span className="text-lg font-semibold text-green-400 truncate">
                   {c.name} Department
                </span>
              </div>

            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Categories;

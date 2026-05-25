import { useEffect, useState } from "react";
import axios from "axios";

// 1. Interfaz basada exactamente en tu modelo de Django
interface Product {
  id: number;
  name: string;
  price: string; // Django DecimalField suele llegar como string en JSON para evitar pérdidas de precisión
  stock: number;
  category: number; // Llega el ID de la categoría correlacionada
  created_at: string;
}

function Products() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/products/")
      .then((res) => {
        setProducts(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching products:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-gray-900 text-white">
        <p className="text-xl animate-pulse">Loading products...</p>
      </div>
    );
  }

  return (
    <div className="p-10 text-white bg-gray-900 min-h-screen">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">AuraCart Products</h1>
        <span className="bg-blue-500/20 text-blue-400 border border-blue-500/30 px-3 py-1 rounded-full text-sm font-medium">
          Total: {products.length} items
        </span>
      </div>

      {products.length === 0 ? (
        <p className="text-gray-400 italic">No products found. Add some in Django Admin!</p>
      ) : (
        // Usamos un grid responsivo para organizar las tarjetas de productos
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {products.map((p) => (
            <div 
              key={p.id} 
              className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-md flex flex-col justify-between transition-all hover:border-blue-500/50 hover:shadow-lg"
            >
              {/* Bloque Superior: Nombre e Info General */}
              <div>
                <div className="flex justify-between items-start mb-2">
                  <h2 className="text-2xl font-semibold text-blue-400 truncate pr-2" title={p.name}>
                    {p.name}
                  </h2>
                  <span className="text-xs bg-gray-700 text-gray-300 font-mono px-2 py-0.5 rounded">
                    #{p.id}
                  </span>
                </div>
                
                <p className="text-sm text-gray-400 mb-4">
                  Added on: {new Date(p.created_at).toLocaleDateString()}
                </p>
              </div>

              {/* Bloque Inferior: Detalles de Venta (Precio y Stock) */}
              <div className="mt-4 pt-4 border-t border-gray-700/60 flex justify-between items-center">
                
                {/* Precio */}
                <div className="flex flex-col">
                  <span className="text-xs font-bold uppercase tracking-widest text-gray-400 mb-0.5">
                    Price
                  </span>
                  <span className="text-2xl font-bold text-green-400">
                    ${parseFloat(p.price).toFixed(2)}
                  </span>
                </div>

                {/* Stock con alerta de color si está bajo */}
                <div className="bg-gray-700/40 p-2 rounded-lg border border-gray-600/50 w-32 text-right">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-gray-400 block mb-0.5">
                    Stock Available
                  </span>
                  <span className={`text-base font-semibold ${p.stock <= 5 ? 'text-red-400 animate-pulse' : 'text-blue-300'}`}>
                    {p.stock} units
                  </span>
                </div>

              </div>

            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Products;

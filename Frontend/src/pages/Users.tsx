import { useEffect, useState } from "react";
import axios from "axios";

interface User {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  address: string;
  birth_date: string;
  role: string;
}

function Users() {

  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/api/users/")

      .then((res) => {

        setUsers(res.data);
        setLoading(false);

      })

      .catch((err) => {

        console.error("Error fetching users:", err);
        setLoading(false);

      });

  }, []);

  if (loading) {

    return (

      <div className="flex justify-center items-center min-h-screen bg-gray-900 text-white">

        <p className="text-xl animate-pulse">
          Loading users...
        </p>

      </div>

    );
  }

  return (

    <div className="p-10 text-white bg-gray-900 min-h-screen">

      <h1 className="text-4xl font-bold mb-6">
        AuraCart Users
      </h1>

      <div className="space-y-4">

        {users.length === 0 ? (

          <p className="text-gray-400 italic">
            No users found. Create some in Django Admin!
          </p>

        ) : (

          users.map((u) => (

            <div
              key={u.id}
              className="bg-gray-800 p-6 rounded-xl border border-gray-700 shadow-md flex justify-between items-center transition-all hover:border-blue-500/50"
            >

              {/* Izquierda */}

              <div className="space-y-2">

                <h2 className="text-2xl font-semibold text-blue-400">

                  {u.first_name} {u.last_name}

                </h2>

                <p className="text-gray-400 text-sm">

                  Username:

                  <span className="text-gray-200 font-mono ml-2">

                    @{u.username}

                  </span>

                </p>

                <p className="text-gray-400 text-sm">

                  Email:

                  <span className="text-gray-200 ml-2">

                    {u.email}

                  </span>

                </p>

                <p className="text-gray-400 text-sm">

                  Address:

                  <span className="text-gray-200 ml-2">

                    {u.address || "No address registered"}

                  </span>

                </p>

                <p className="text-gray-400 text-sm">

                  Birth Date:

                  <span className="text-gray-200 ml-2">

                    {u.birth_date || "Not provided"}

                  </span>

                </p>

              </div>

              {/* Derecha */}

              <div className="bg-gray-700/60 p-4 rounded-xl border border-gray-600 w-64 min-h-[120px] flex flex-col justify-center shadow-inner">

                <span className="text-xs font-bold uppercase tracking-widest text-gray-400 block mb-2">

                  Account Role

                </span>

                <span className={`text-lg font-semibold ${
                  u.role === 'ADMIN'
                    ? 'text-red-400'
                    : 'text-green-400'
                }`}>

                  {u.role}

                </span>

                <p className="text-gray-400 text-sm mt-3">

                  User ID:

                  <span className="font-mono text-gray-200 ml-2">

                    #{u.id}

                  </span>

                </p>

              </div>

            </div>

          ))

        )}

      </div>

    </div>
  );
}

export default Users;
import "./App.css";

function App() {
  return (
    <>
      <nav className="w-screen h-[75px] shadow-xl">
        <div className="w-[1300px]  h-full m-auto flex justify-between">
          {/* left hand side */}
          <div className="w-[20%] h-full flex justify-center items-center">
            <p className="font-extrabold text-2xl text-blue-500">
              PYTHON <span className="text-orange-500">BATCH</span>
            </p>
          </div>
          {/* right hand side */}
          <div className="w-[40%] h-full flex items-center">
            <ul className="w-full h-full flex justify-between items-center">
              <li className="text-xl font-semibold hover:text-orange-500 hover:cursor-pointer">
                Home
              </li>
              <li className="text-xl font-semibold hover:text-orange-500 hover:cursor-pointer">
                Service
              </li>
              <li className="text-xl font-semibold hover:text-orange-500 hover:cursor-pointer">
                Contact Us
              </li>
              <li className="text-xl font-semibold hover:text-orange-500 hover:cursor-pointer">
                Blogs
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="w-[450px] p-4 shadow-2xl rounded-xl m-auto mt-10">
        <h1 className="text-center text-xl font-bold">Login Page</h1>
        <div className="p-4">
          <input
            type="email"
            placeholder="Enter your email"
            className="w-full p-2 border-none outline-none border-b-2 border-solid border-blue-500"
          />
        </div>
        <div className="p-4">
          <input
            type="password"
            placeholder="Enter your password"
            className="w-full p-2 border-none outline-none border-b-2 border-solid border-blue-500"
          />
        </div>

        <p className="text-end p-2 underline text-gray-700 cursor-pointer">
          forget password
        </p>

        <button className="bg-purple-500 w-full p-2 text-white rounded hover:bg-purple-400 cursor-pointer">
          Login
        </button>
        <p className="text-center mt-2 text-gray-700">
          If no account{" "}
          <span className="text-blue-500 underline cursor-pointer">
            Register
          </span>
        </p>
      </div>

      {/*grid */}

      <div className="w-[450px] h-[400px] p-4 grid  grid-cols-2 grid-rows-3 m-auto mt-10 gap-2 border border-solid border-amber-400">
        <div className="shadow-2xl">
          <img
            src="https://img.magnific.com/free-photo/closeup-shot-beautiful-ginger-domestic-kitten-sitting-white-surface_181624-35913.jpg?semt=ais_hybrid&w=740&q=80"
            alt=""
            className="w-full h-full "
          />
        </div>
        <div className="shadow-2xl">
          <img
            src="https://img.magnific.com/free-photo/closeup-shot-beautiful-ginger-domestic-kitten-sitting-white-surface_181624-35913.jpg?semt=ais_hybrid&w=740&q=80"
            alt=""
            className="w-full h-full "
          />
        </div>
        <div className="shadow-2xl">
          <img
            src="https://img.magnific.com/free-photo/closeup-shot-beautiful-ginger-domestic-kitten-sitting-white-surface_181624-35913.jpg?semt=ais_hybrid&w=740&q=80"
            alt=""
            className="w-full h-full "
          />
        </div>
        <div className="shadow-2xl">
          <img
            src="https://img.magnific.com/free-photo/closeup-shot-beautiful-ginger-domestic-kitten-sitting-white-surface_181624-35913.jpg?semt=ais_hybrid&w=740&q=80"
            alt=""
            className="w-full h-full "
          />
        </div>
        <div className="shadow-2xl">
          <img
            src="https://img.magnific.com/free-photo/closeup-shot-beautiful-ginger-domestic-kitten-sitting-white-surface_181624-35913.jpg?semt=ais_hybrid&w=740&q=80"
            alt=""
            className="w-full h-full "
          />
        </div>
        <div className="shadow-2xl">
          <img
            src="https://img.magnific.com/free-photo/closeup-shot-beautiful-ginger-domestic-kitten-sitting-white-surface_181624-35913.jpg?semt=ais_hybrid&w=740&q=80"
            alt=""
            className="w-full h-full "
          />
        </div>
      </div>
    </>
  );
}

export default App;

       
       

    
  

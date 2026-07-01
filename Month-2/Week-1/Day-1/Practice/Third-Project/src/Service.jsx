import React from "react";

function Service({obj,children}) {
  return (
    <div>
        Service
        <br />
        object Email :{obj.email}
         <br />
         object password :{obj.password}
         {children}
    </div>
  );
}

export default Service;
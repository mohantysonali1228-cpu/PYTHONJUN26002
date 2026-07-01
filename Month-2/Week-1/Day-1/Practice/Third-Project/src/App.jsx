import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Home from './Home'
import Service from './Service'
import Card from './Card'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      
    hello
   
    <Home name={"sonali"} isPassed={true}/>
    <Service obj={{email:"hello@gmail.com",password:"hello@123"}}
    >
      <h1>Hello this is H1 tag </h1>
      <b> this is the bold tag</b>
      
    </Service>
    <div>className='w-[1200px] p-2  m-auto bg-amber-300 grid grid-cols-3'</div>
    <Card  cardDate={{img:"",tittle:"",desc:""}}/>
    <Card cardDate={{img:"",tittle:"",desc:""}}/>
    <Card cardDate={{img:"",tittle:"",desc:""}}/>
    <Card cardDate={{img:"",tittle:"",desc:""}}/>
    <Card cardDate={{img:"",tittle:"",desc:""}} />

    </>
  )
}

export default App;

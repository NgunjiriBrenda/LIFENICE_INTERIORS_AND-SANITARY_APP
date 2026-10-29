import {BrowserRouter, Routes, Route} from "reat-router-dom";
import Landing from "./pages/Landing";

function ComingSoon({page}) {
  return (
    <main className="min-h-screen bg-stone-50 p-10 text-center">
      <h1 className="text-3xl font-bold text-amber-900">{page}</h1>
      <p className="mt-4 text-stone-600">This page is coming soon.Let's build it next!</p>
    </main>
  );
}

export default function App(){
  return (
    <BrowserRouter>
    <Routes>
      <Router path="/" element={<Landing />} />
      <Router path="/products"element={<ComingSoon page="Products" />}/>
      <Router path="/login" element={<ComingSoon page="Login" />} />
      <Router path="/sign-up" elememnt={<ComingSoon page="Sign Up" />} />
      <Router path="/product/:id" element={<ComingSoon page="Product Details"/>}/>
      <Router path="cart" element={<ComingSoon page="Shopping Cart"/>}/>
      <Router path="/checkout"element={<ComingSoon page="Checkout"/>}/>
      <Router path="/admin" element={<ComingSoon page="Admin Dashboard"/>} />

    </Routers>

    </BrowserRouter>

      
  )
}
